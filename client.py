# Import socket module
import socket

try:
    # Create a socket object
    s = socket.socket()

    # Define the port on which you want to connect
    port = 12345

    # connect to the server on local computer
    s.connect(('127.0.0.1', port))

    # receive data from the server
    print(s.recv(1024).decode())

    l = ""
    print("enter number1 +/-/*/'/'(sign) + number2 or end to , enter 'end' to end the process")
    while (l != "end"):
        l = input()
        s.send(l.encode())
        print(s.recv(1024).decode())
    s.close()
except:
    print("some goes wrong...")


