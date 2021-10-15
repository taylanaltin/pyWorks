import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    """Try to connect the server if there exists a hosts"""
    s.connect((socket.gethostname(),1234))
    while True:
        message = s.recv(1024)
        mstr = message.decode("utf-8")
        if mstr == "q":
            print("Program Close Key Detected")
            break
        print(mstr)
    s.close()
except socket.error as msg:
    print(msg)
    print("Run the server first!")
    input()