# Riley Barnes
# cs455
# hw4

# import socket module
from socket import *
from _thread import *
import threading
import time # used for testing
import sys  # In order to terminate the program


filelock = threading.Lock()
tnum = 0


def threadjob(connection, thread):
    try:
        # print("[D] i got in to try...")

        print("[+]trying to send hello %d...." % thread )
        #time.sleep(10)

        message = connection.recv(1024).decode()  # Fill in start #Fill in end
        filename = message.split()[1]
        f = open(str(filename[1:]))
        outputdata = f.read()  # Fill in start #Fill in end
        filelock.release()
        print("[+]file read ready to send %d...." % thread)
        # Send one HTTP header line into socket

        # print(outputdata)
        # Fill in start
        header = "HTTP/1.x 200 OK\n\n"
        outputdata = header + outputdata
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connection.send(outputdata[i].encode())
        connection.send("\r\n".encode())
        print("[+]message sent...")
        connection.close()
        print("[*] connection closed...")
    except IOError:
        print("[-]file was not found...")
        # print("[D] somthing went wrong...")
        # Send response message for file not found
        # Fill in start
        filelock.release()
        header = "HTTP/1.x 404 NOT FOUND\n\n"
        connection.send(header.encode())

        # Fill in end
        # Close client socket
        # Fill in start
        connection.close()
        print("[*] connection closed...")
        # Fill in end

    return


serverSocket = socket(AF_INET, SOCK_STREAM)
printlock = threading.Lock()
# Prepare a sever socket
# Fill in start

serverPort = 8081
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print("[+] Server ready to Receive......")

# Fill in end
while True:
    # Establish the connection
    connectionSocket, addr = serverSocket.accept()
    filelock.acquire()
    print("[+]connection established....")
    tnum += 1
    start_new_thread(threadjob, (connectionSocket, tnum))


serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding dat
