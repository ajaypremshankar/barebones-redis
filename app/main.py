import socket  # noqa: F401
import threading
from dataclasses import dataclass


@dataclass
class FiredCommand:
    command: str
    params: [str] = None


def encode_resp(raw_resp: str):
    return f"+{raw_resp}\r\n".encode()


def parse_command(raw_command: str):
    raw_command_arr = raw_command.split("\r\n")
    command_and_param_length = int(raw_command_arr[0].replace("*", "")) if raw_command_arr[0].startswith("*") else 0
    if command_and_param_length == 0 or len(raw_command_arr) < 4:
        raise Exception("Invalid command")

    command = raw_command_arr[2]
    params_length = command_and_param_length - 1

    params = []
    if params_length > 0:
        for index in range(params_length):
            params.append(raw_command_arr[index * 2 + 4])  # first param start at index 4, if available.

    return FiredCommand(command, params)


def spawn_requests(client: socket.socket):
    connected = True
    while connected:
        command = client.recv(1024).decode()
        fired_command = parse_command(command)

        match fired_command.command.lower():
            case 'ping':
                client.send(encode_resp("PONG"))
            case 'echo':
                client.send(encode_resp(fired_command.params[0]))

        connected = bool(command)


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        client, address = server_socket.accept()  # wait for client
        t = threading.Thread(target=lambda: spawn_requests(client))
        t.start()


if __name__ == "__main__":
    main()
