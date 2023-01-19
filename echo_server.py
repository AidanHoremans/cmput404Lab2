import socket
from threading import Thread

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
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        s.listen()

        conn, addr = s.accept()
        handle_connection(conn, addr)
    return

def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSock:
        serverSock.bind((HOST, PORT))
        serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serverSock.listen() 

        while True:
            conn, addr = serverSock.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()

start_server()