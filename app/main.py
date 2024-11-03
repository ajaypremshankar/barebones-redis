import socket  # noqa: F401
import threading

def spawn_requests(client: socket.socket):
    connected = True
    while connected:
        command = client.recv(1024).decode()
        connected = bool(command)
        if 'ping' in command.lower():
            client.send(b"+PONG\r\n")


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        client, address = server_socket.accept()  # wait for client
        t = threading.Thread(target=lambda: spawn_requests(client))
        t.start()

if __name__ == "__main__":
    main()
