from detect import *
from GUI import *
import tkinter as tk
import cv2
NonOK = "./NonOK"

count = 0
det = detect()


A1 = App()

# y = det.saved(Screen)
# A1.switch(y)
x = det.saved(NonOK)

while count < 2:
    det.predictimg(x)
    count += 1

