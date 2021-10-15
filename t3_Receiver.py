import socket
from PIL import Image
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((socket.gethostname(), 1234))  #Connect to server if exists
    now = datetime.now()
    sent_time = now.strftime("%H%M%S")
    while True:
        file = open(f"Received_{sent_time}.png", 'wb')
        image_chunk = s.recv(1024)
        while image_chunk:
            file.write(image_chunk)
            image_chunk = s.recv(1024)
        break
    file.close()
    imLoad = Image.open(f"Received_{sent_time}.png")
    imLoad.show()
    imLoad.close()
    s.close()
except socket.error as msg:
    print(msg)
    print("Run the server first!")
    input()
