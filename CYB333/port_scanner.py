import socket
import time

def scan_ports(target, start_port, end_port):
    print(f"\n[SCAN START] Target: {target}")
    print(f"Scanning ports {start_port} to {end_port}\n")

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
            else:
                print(f"[CLOSED] Port {port}")

            sock.close()
            time.sleep(0.2)  # ethical delay

        except Exception as e:
            print(f"[ERROR] {e}")

if __name__ == "__main__":
    try:
        target = input("Enter target (127.0.0.1 or scanme.nmap.org): ")
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))

        if start_port < 0 or end_port > 65535:
            raise ValueError("Invalid port range")

        scan_ports(target, start_port, end_port)

    except ValueError:
        print("[ERROR] Invalid port numbers")
    except socket.gaierror:
        print("[ERROR] Host unreachable")