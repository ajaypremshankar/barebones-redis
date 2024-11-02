import socket  # noqa: F401


def main():
    # Uncomment this to pass the first stage
        server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
        client, address = server_socket.accept()  # wait for client
        while True:
            command = client.recv(1024).decode()
            if 'ping' in command.lower():
                client.send(b"+PONG\r\n")

if __name__ == "__main__":
    main()
