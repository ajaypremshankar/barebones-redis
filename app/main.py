import socket  # noqa: F401
import threading

from app import command_parser


def spawn_requests(client: socket.socket):
    while True:
        command = client.recv(1024).decode()
        if not bool(command):
            break

        redis_command = command_parser.parse(command)
        redis_command.execute(client)


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        client, address = server_socket.accept()  # wait for client
        t = threading.Thread(target=lambda: spawn_requests(client))
        t.start()


if __name__ == "__main__":
    main()
