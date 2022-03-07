#Riley Barnes
#cs455

#import socket module
from socket import *
import sys # In order to terminate the program
#todo add threading
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort = 8081
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("[+] Server ready to Receive......")

#Fill in end
while True:
    #Establish the connection
    #print("[D] im here....")
    connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
    print("[+]connection established....")
    #print("[D] im here....")
    try:
        #print("[D] i got in to try...")
        print("[+]trying to send hello....")
        message = connectionSocket.recv(1024).decode()#Fill in start #Fill in end
        filename = message.split()[1]
        f = open(str(filename[1:]))
        outputdata = f.read()#Fill in start #Fill in end
        print("[+]file read ready to send....")
        #Send one HTTP header line into socket

        # print(outputdata)
        #Fill in start
        header = "HTTP/1.x 200 OK\n\n"
        outputdata = header + outputdata
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        print("[+]message sent..." )
        connectionSocket.close()
        print("[*] connection closed...")
    except IOError:
        print("[-]file was not found...")
        #print("[D] somthing went wrong...")
        #Send response message for file not found
        #Fill in start
        header = "HTTP/1.x 404 NOT FOUND\n\n"
        connectionSocket.send(header.encode())

        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        print("[*] connection closed...")
        #Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding dat

