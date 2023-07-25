import socket

import argparse



SERVER_IP = "127.0.0.1"
SERVER_PORT = 80
parser = argparse.ArgumentParser(description="The client of HTTP/")
parser.add_argument("host", nargs="?", default=SERVER_IP, help="The address where you will listened(127.0.0.1 default)")
parser.add_argument("port", nargs="?", default=SERVER_PORT, type=int, help="The port to connect to(6789 default)")
parser.add_argument("filename", nargs="?", default="HelloWorld.html", help="The file on the host to retrieve")
arguments = parser.parse_args()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket1:
    socket1.connect((arguments.host, arguments.port))
    http_request = "GET /{} HTTP/1.1".format(arguments.filename)
    socket1.sendall(http_request.encode("utf-8"))
    response = ""
    connection= True

    while connection:
        dataInfo = socket1.recv(4096)
        if not dataInfo:
            break
        else:
            response += dataInfo.decode("utf-8")

    print(response)