import socket, requests

BYTES = 4096
HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by: " + addr)
        while True:
            data = conn.recv(BYTES)
            if not data:
                break
            print(data)
            conn.send(data)
        


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #SOL_SOCKET = socket level, and we reuse the address -> how do we reuse a port? tells the operating system to allow us to use this even if the socket is in timeout
        
        s.listen()

        conn, addr = s.accept()
        handle_connection(conn, addr)
    return

start_server()