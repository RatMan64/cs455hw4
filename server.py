#Riley Barnes
#cs455

#import socket module
from socket import *
import sys # In order to terminate the program
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
    print("[D] im here....")
    connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
    print("[D] im here....")
    try:
        print("[D] i got in to try...")
        message = connectionSocket.recv(1024).decode()#Fill in start #Fill in end
        filename = message.split()[1]
        f = open(str(filename[1:]))
        outputdata = f#Fill in start #Fill in end
        #Send one HTTP header line into socket
        print(outputdata)
        #Fill in start


        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        print("[D] somthing went wrong...")
        #Send response message for file not found
        #Fill in start
        header = "POST "
        errormessage ="<html><body><header><h1>404 Not Found</h1></header></body></html>"
        errormessage = errormessage
        for i in range(0, len(errormessage)):
            connectionSocket.send(errormessage[i].encode())
        connectionSocket.send("\r\n".encode())
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
    serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding dat

