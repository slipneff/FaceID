import os
import cv2
import tkinter
import PIL
import face_recognition
import cryptocode
from tkinter import *
from PIL import Image,ImageTk

class App():
    def Identify(self):
        ret, img = self.vid.get_frame()
        face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        wait_img = cv2.imread('source.png')
        #crop_img = cv2.cvtColor(wait_img, cv2.COLOR_BGR2GRAY)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)  # нахождение лица на картинке с камеры
        #print(faces)
        for (x, y, w, h) in faces:  # обрезка
            crop_img = img[y:y + h, x:x + w]
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        path = 'C:/Users/slipn/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/FaceID/'
        IDENTITY = len([f for f in os.listdir(path)
                        if os.path.isfile(os.path.join(path, f))])
        #print(IDENTITY)
        try:
            for i in range(0, IDENTITY):
                image_enc1 = face_recognition.face_encodings(crop_img)[0]
                image_2 = face_recognition.load_image_file(path+f"img/source{i}.png")
                image_enc2 = face_recognition.face_encodings(image_2)[0]
                result = face_recognition.compare_faces([image_enc1], image_enc2)
                if result[0]:
                    #print("helo")
                    self.window.destroy()
                    taskmanager_on()
        except:
            pass
        passkey = 'denchik'
        with open(path+'pass', 'r') as f:
            password_raw = f.readlines()
        if self.message.get() == cryptocode.decrypt(''.join(password_raw), passkey):
            print("helo")
            self.window.destroy()

    def __init__(self, window, window_title, video_source=0):
       self.window = window
       self.window.title(window_title)
       self.video_source = video_source
       self.vid = MyVideoCapture(self.video_source)
       self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
       self.canvas.pack()
       self.label = tkinter.Label(window, text="Press the button", font="Arial 15", width=45)
       window.attributes("-fullscreen", True)
       self.label.pack()
       self.message = StringVar()
       self.entry = tkinter.Entry(window, font="Arial 20", textvariable=self.message)
       self.entry.pack()
       self.button = tkinter.Button(window,text="Submit",command=self.Identify)
       self.button.pack()
       self.delay = 15
       self.update()
       self.window.mainloop()

    def update(self):
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        self.window.after(self.delay, self.update)



class MyVideoCapture:
   def __init__(self, video_source=0):
       self.vid = cv2.VideoCapture(video_source, cv2.CAP_DSHOW)
       if not self.vid.isOpened():
           raise ValueError("Unable to open video source", video_source)

       self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
       self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
       self.get_frame()
   def get_frame(self):
       if self.vid.isOpened():
           ret, frame = self.vid.read()
           frame = cv2.flip(frame, 1)
           #cv2.imshow('FaceID', frame)
           if ret:
               return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
           else:
               return (ret, None)
       else:
           return (None)

def taskmanager_off():
    path1 = "C:\Windows\System32\Taskmgr.exe"
    path2 = "C:\Windows\System32\Taskmgr1.exe"

    os.system("takeown /f C:\Windows\System32\Taskmgr.exe")
    os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Администраторы:F /c /l")
    os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Пользователи:F /c /l")

    os.system("taskkill /im taskmgr.exe")
    os.rename(path1, path2)

def taskmanager_on():
    path1 = "C:\Windows\System32\Taskmgr.exe"
    path2 = "C:\Windows\System32\Taskmgr1.exe"
    os.rename(path2, path1)


App(tkinter.Tk(), "FaceID")