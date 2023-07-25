from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
serverPort=6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end

while True:
	#Establish the connection

	print ('Ready to serve...')

	connectionSocket, addr = serverSocket.accept() 

	try:

		message = connectionSocket.recv(1024)  

		nameOfFile = message.split()[1]
		
		f = open(nameOfFile[1:])

		outputdata = f.read() 
		print (outputdata)

		#Send one HTTP header line into socket

		#Fill in start#
		connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
		#Fill in end

		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		
		connectionSocket.send("\r\n".encode())

		connectionSocket.close()

	except IOError:
		# Send HTTP response message for file not found
		#Fill in start
		connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
		#Fill in end
		# Close the client socket
        #Fill in start
		connectionSocket.close()
		#Fill in end
serverSocket.close()
sys.exit()