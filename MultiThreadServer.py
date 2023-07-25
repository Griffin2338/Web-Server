import threading
import argparse
import socket

parser = argparse.ArgumentParser(description="Server(HTTP) with Threat\n")
parser.add_argument("server_ip", nargs="?", default="192.168.1.124", help="The address where you will listened(192.168.1.124 default)")
parser.add_argument("server_port", nargs="?", default=6789,help="The port to connect to(6789 default)")
args = parser.parse_args()
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(("192.168.1.124", 6789))
serverSocket.listen(4)


def serve(sock, addr):

    print("\n {} sent request".format(addr))

    try:

        receiveMessage = sock.recv(2048)
        request = receiveMessage.decode().split("\r\n")[0]
        nameOfFile = request.split()[1]
        nameOfFile = "HelloWorld.html" if nameOfFile == "/" else nameOfFile[1:]
        print("request: {}".format(receiveMessage.decode().strip("\r\n\n")))

        with open(nameOfFile, "r") as f:
            LastData = f.read()


        response = ("HTTP/1.1 200 OK\n"
                    "Server: Python 3.9.8\n"
                    "Content-Type: text/html; charset=utf-8\r\n\n")
        sock.send(response.encode())
        for i in range(0, len(LastData)):
            sock.send(LastData[i].encode())

        sock.send("\r\n".encode())
        sock.close()

    except IOError:
        response = ("HTTP/1.1 404 Not Found\n"
                    "Server: Python 3.9.8\n"
                    "Content-Type: text/html; charset=utf-8\r\n\n")
        sock.send(response.encode())
        sock.send("\r\n".encode())
        sock.close()

print("The server(HTTP) listening the {}:{}".format(args.server_ip, args.server_port))

connection= True
while connection:
    cli_sock, addr = serverSocket.accept()
    threading.Thread(target=serve, args=(cli_sock, addr)).start()