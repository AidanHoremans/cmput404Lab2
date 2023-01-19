import socket

BYTES = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHost: " + host.encode('utf-8') + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))
    s.send(request)
    s.shutdown(socket.SHUT_WR)

    #listen for response
    response = s.recv(BYTES)

    while len(response) > 0:
        print(response)
        response = s.recv(BYTES)

    s.close()

get("www.google.com", 80)
