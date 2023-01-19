import socket
from threading import Thread

BYTES = 4096
HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        request = b''
        while True:
            data = conn.recv(BYTES)
            if not data:
                break
            print(data)
            request += data
        response = send_request("www.google.com", 80, request)
        conn.sendall(response)
    return

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSock:
        serverSock.bind((HOST, PORT))
        serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        serverSock.listen(2) #tells socket how many requests to queue up

        conn, addr = serverSock.accept()

        handle_connection(conn, addr)


    return

def send_request(host, port, requestData):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSock:
        clientSock.connect((host, port))
        clientSock.send(requestData)
        clientSock.shutdown(socket.SHUT_WR)

        data = clientSock.recv(BYTES)

        result = b'' + data
        while len(data):
            data = clientSock.recv(BYTES)
            result += data
        
        return result


def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSock:
        serverSock.bind((HOST, PORT))
        serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serverSock.listen(2) #tells socket how many requests to queue up

        while True:
            conn, addr = serverSock.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()


#start_server()
start_threaded_server()