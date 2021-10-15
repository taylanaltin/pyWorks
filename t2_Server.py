import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print("Waiting connection from client")
while True:
    clientsocket, adress = s.accept()
    """Client is connected"""
    print(f"Connection from {adress} has been established")
    print("Input 'q' for stop the program")
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
    while True:
        """Gets input from user until the q key is pressed."""
        inputstring = input("Enter the string \n")
        clientsocket.send(bytes(inputstring, "utf-8"))
        if inputstring == "q":
            print("q pressed, ending loop")
            clientsocket.close()
            break
    break
