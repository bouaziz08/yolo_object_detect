import tkinter as tk
from tkinter import *
import cv2, time, os
from PIL import Image, ImageTk
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import QUrl
import glob

class App:
    def __init__(self, video_source=0):
        self.window = Tk()
        self.window.title("APPD")

        self.window.resizable(1, 1)
        self.window['bg'] = 'black'
        self.video_source = video_source


        self.vid = GUI(self.video_source)

        self.canvas = Canvas(self.window, width=self.vid.width, height=self.vid.height, bg='red')
        self.canvas.pack()

        self.btn_snapshot = tk.Button(self.window, text="snapshot", width=20, bg="goldenrod2", activebackground='red', command=self.snapshot)
        self.btn_snapshot.pack(anchor=W, expand=True)

        self.btn_snapshot = tk.Button(self.window, text="Open", width=20, bg="goldenrod2", activebackground='red', command=self.windows)
        self.btn_snapshot.pack(anchor=E, expand=True, pady=0, padx=0)

        self.update()
        self.window.mainloop()

    def saved(self, folder):
        if not os.path.exists(folder):
            raise ValueError("Folder does not exist.")

        files = os.listdir(folder)
        # Filter out non-image files (e.g., subdirectories)
        image_files = [file for file in files if file.lower().endswith(('.jpg'))]
        if not image_files:
            raise ValueError("No image files found in the folder.")

        # Sort the image files based on their modification time (most recent first)
        sorted_image_files = sorted(image_files, key=lambda x: os.path.getmtime(os.path.join(folder, x)), reverse=True)
        # Return the path to the last (most recently saved) image
        last_saved_image = os.path.join(folder, sorted_image_files[0])
        return last_saved_image

    # def switch(self, im):
    #     i = 0
    #     inputFolder = 'Screen'
    #     for img in glob.glob(im):
    #         image = cv2.imread(img)
    #         imgResized = cv2.resize(image, (1066, 600))
    #         cv2.imwrite("./NonOK/IMG-" + time.strftime("%H-%M-%S-%d-%m") + ".png", imgResized)
    #         i += 1

    def snapshot(self):
        check, frame = self.vid.getFrame()
        if check:
            image = "./Screen"+"/IMG-" + time.strftime("%H-%M-%S-%d-%m") + ".jpg"
            cv2.imwrite(image, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            image = "./NonOK" + "/IMG-" + time.strftime("%H-%M-%S-%d-%m") + ".jpg"
            cv2.imwrite(image, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))


            # msg = Label(self.window, text='image saved '+image, bg='black', fg='green').place(x=430, y=510)


    def windows(self):
        OK = './OK'
        self.im = Image.open(self.saved(OK))
        self.im.show()

    def update(self):
        isTrue, frame = self.vid.getFrame()

        if isTrue:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.window.after(15, self.update)



class GUI:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)

        if not self.vid.isOpened():
            raise ValueError("Unable to open camera!!!!!", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.vid.release()
        self.vid = cv2.VideoCapture(video_source)

        self.new_width = 740
        self.new_height = 580
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, self.new_width)
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, self.new_height)
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(self.height)
        print(self.width)

    def getFrame(self):
        if self.vid.isOpened():
            isTrue, frame = self.vid.read()

            if isTrue:
                return (isTrue, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (isTrue, None)


    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


