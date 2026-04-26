import socket

HOST = '127.0.0.1'
PORT = 65432

def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(1)

        print(f"[SERVER] Listening on {HOST}:{PORT}...")

        conn, addr = server.accept()
        print(f"[SERVER] Connected by {addr}")

        while True:
            data = conn.recv(1024)
            if not data:
                print("[SERVER] Client disconnected.")
                break

            message = data.decode()
            print(f"[SERVER RECEIVED] {message}")

            response = f"Server received: {message}"
            conn.sendall(response.encode())

        conn.close()

    except Exception as e:
        print(f"[SERVER ERROR] {e}")

if __name__ == "__main__":
    start_server()