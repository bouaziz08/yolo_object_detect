import tkinter
from tkinter import *
from PIL import Image, ImageDraw, ImageFont

import cv2

# Replace 'your_ip_address' with the IP address of your camera
# camera_url = 0
#
# # Open the IP camera stream
# cap = cv2.VideoCapture(camera_url)
#
# # Check if the camera stream is opened successfully
# if not cap.isOpened():
#     print("Error: Could not open camera.")
#     exit()
#
# # Get the current frame width
# current_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# current_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print("Current Frame Width:", current_width)
# print("Current Frame height:", current_height)
# # Specify the new frame width
# new_width = 350  # Replace this with your desired new width
#
# # Set the new frame width
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, new_width)
#
# # Verify the change
# updated_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# print("Updated Frame Width:", updated_width)
#
# # Read and display frames (optional)
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     cv2.imshow("IP Camera", frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release the camera and close the display window
# cap.release()
# cv2.destroyAllWindows()
# inputFolder = 'NonOK'
#
# i = 0
#
# for img in glob.glob(inputFolder + "/*.jpg"):
#     image = cv2.imread(img)
#     imgResized = cv2.resize(image, (750, 600))
#     cv2.imwrite("Resized Folder/image%04i.jpg" %i, imgResized)
#
#     i += 1
#
# cv2.destroyAllWindows()
# def test():
#     OK = './OK'
#     im = Image.open("./OK/IMG-09-42-15-09-08.jpg")
#     im.show()
#
# test()

img = Image.open('0_12.jpg')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Add Text to an image
I1.text((100, 100), "nice Car", fill=(255, 100, 10))

# Display edited image
img.show()


