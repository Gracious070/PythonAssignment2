import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((HOST, PORT))

    message = "Hello from client!"

    client_socket.sendall(message.encode())

    print("Message sent successfully.")

except OSError as error:
    print("Network error:", error)

finally:
    client_socket.close()
    print("Client closed.")