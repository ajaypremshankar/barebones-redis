import socket  # noqa: F401
import sys
import threading

from app import command_parser
from app.globaldatastore import GlobalConfigStore


def spawn_requests(client: socket.socket):
    while True:
        command = client.recv(1024).decode()
        if not bool(command):
            break

        redis_command = command_parser.parse(command)
        redis_command.execute(client)


def parse_args():
    if len(sys.argv) <= 1:
        return {}

    args = sys.argv[1:]
    i = 0

    args_dict = {}

    while i < len(args):
        if args[i].startswith("--") and i + 1 < len(args):
            args_dict[args[i].replace("--", "").lower()] = args[i + 1]
            i += 2
        else:
            args_dict[args[i].lower()] = True
            i += 1

    return args_dict


def main():
    GlobalConfigStore.set_config(parse_args())

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        client, address = server_socket.accept()  # wait for client
        t = threading.Thread(target=lambda: spawn_requests(client))
        t.start()


if __name__ == "__main__":
    main()
