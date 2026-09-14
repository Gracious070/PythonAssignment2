import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("Server is waiting for a connection...")

    connection, address = server_socket.accept()

    with connection:
        print("Client connected:", address)

        message = connection.recv(1024).decode()

        print("Message received:", message)

except OSError as error:
    print("Network error:", error)

finally:
    server_socket.close()
    print("Server closed.")