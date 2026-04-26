import socket

HOST = '127.0.0.1'
PORT = 65432

def start_client():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))

        print("[CLIENT] Connected to server.")

        message = input("Enter message: ")
        client.sendall(message.encode())

        response = client.recv(1024)
        print(f"[CLIENT RECEIVED] {response.decode()}")

        client.close()
        print("[CLIENT] Connection closed.")

    except ConnectionRefusedError:
        print("[CLIENT ERROR] Server is not running.")
    except Exception as e:
        print(f"[CLIENT ERROR] {e}")

if __name__ == "__main__":
    start_client()