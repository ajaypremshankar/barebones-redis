import socket  # noqa: F401


def main():
    # Uncomment this to pass the first stage
    while True:
        server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
        client, address = server_socket.accept() # wait for client

        client.send(b"+PONG\r\n")
        client.close()

if __name__ == "__main__":
    main()
