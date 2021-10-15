import socket
from tkinter import filedialog
from PIL import Image,ImageTk
import os
def Gui():

    #Gui construction
    filePath = filedialog.askopenfilename(filetypes=[("Image Files", ".png .jpg")])
    #Selection of file to be croped
    load = Image.open(filePath)
    width, height = load.size
    #load.show()
    print(f"Selected File \nFile Path : {filePath} \nSize : {width}*{height}")
    return filePath,width,height


def Crop(imagepath,width, height):
    load_image = Image.open(imagepath)
    x_final=width/2
    y_final=height/2
    cropped_image = load_image.crop(box = (0,0,x_final,y_final))
    cropped_image.save("t3_CroppedImageBuffer.png")
    cropped_image.close()
    print(f"Cropped File \nTemporary File Name : t3_CroppedImageBuffer.png \nSize : {int (width/2)}*{int (height/2)}")
    load_image.close()

filePath,width,height = Gui() #Selection of the image
Crop(filePath,width,height) #Crop process
imageData= open("t3_CroppedImageBuffer.png","rb") #Open image data sendable from socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Socket parameters
s.bind((socket.gethostname(),1234))
s.listen(5)
print("Image is selected and cropped. Waiting partner to send!")
while True:
    clientsocket, adress = s.accept()
    print(f"Connection from {adress} has been established")
    while True:
        send_data = imageData.read(1024)
        while send_data:
            clientsocket.send(send_data)
            send_data = imageData.read(1024)
        imageData.close()
        print("Data sent")
        break
    break
os.remove("t3_CroppedImageBuffer.png")