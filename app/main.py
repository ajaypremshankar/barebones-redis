import socket  # noqa: F401
import threading

from app import command_parser

data = {}

def encode_resp(raw_resp: str, resp_type = None):
    if not resp_type:
        return f"+{raw_resp}\r\n".encode()
    elif resp_type == 'simple_string':
        return f"${len(raw_resp)}\r\n{raw_resp}\r\n".encode()

def spawn_requests(client: socket.socket):
    connected = True
    while connected:
        command = client.recv(1024).decode()
        fired_command = command_parser.parse(command)

        match fired_command.command.lower():
            case 'ping':
                client.send(encode_resp("PONG"))
            case 'echo':
                client.send(encode_resp(fired_command.params[0]))
            case 'set':
                data[fired_command.params[0]] = fired_command.params[1]
                client.send(encode_resp("OK"))
            case 'get':
                client.send(encode_resp(data[fired_command.params[0]], 'simple_string'))

        connected = bool(command)


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        client, address = server_socket.accept()  # wait for client
        t = threading.Thread(target=lambda: spawn_requests(client))
        t.start()


if __name__ == "__main__":
    main()
