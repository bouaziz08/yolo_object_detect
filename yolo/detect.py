import os, cv2
import shutil, math
from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont
import random, time

class detect:
    def __init__(self):
        self.conf = 0.2
        self.OK = "./OK"
        self.NonOK = "./NonOK"
        self.screen = "./Screen"
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

    def download(self, img, x0, y0, x1, y1):
        tmp = self.saved(self.NonOK)
        processed_image = Image.open(tmp)
        final_image = processed_image.copy()

        # Create a drawing object to add the frame
        draw = ImageDraw.Draw(final_image)

        # Define the frame parameters (you can adjust these values)
        frame_color = "green"
        frame_width = 5
        image_width, image_height = final_image.size
        x0 = self.x1
        y0 = self.y1
        x1 = self.x2
        y1 = self.y2
        # Draw a rectangle as the frame
        frame_rectangle = [
            (x0, y0),
            (x1, y1)
        ]
        coeff = self.conf
        draw.rectangle(frame_rectangle, outline=frame_color, width=frame_width)
        print(coeff)
        myFont = ImageFont.truetype('arial.ttf', 40)
        draw.text((x0, y0), str(coeff), font=myFont)
        draw.text((x1, y0), "Laptop", font=myFont)
        # Save the final image with the frame
        if self.conf > 0.3:
            image = "./OK" + "/IMG-" + time.strftime("%H-%M-%S-%d-%m") + ".jpg"
            final_image.save(image)
            os.remove(tmp)


        # Close the images
        processed_image.close()
        final_image.close()

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

    def switch(self, image):
        os.makedirs(self.OK, exist_ok=True)
        os.makedirs(self.NonOK, exist_ok=True)

        if self.conf > 0.3:
            shutil.move(image, self.OK)


    def load(self, image):
        model_path = os.path.join('.', 'runs', 'detect', 'train9', 'weights', 'best.pt')
        model = YOLO(model_path)
        resultat = model(image)
        for r in resultat:
            boxes = r.boxes
            for box in boxes:
                self.x1, self.y1, self.x2, self.y2 = box.xyxy[0]
                self.x1, self.y1, self.x2, self.y2 = int(self.x1), int(self.y1), int(self.x2), int(self.y2)


                self.conf = math.ceil((box.conf[0] * 100)) / 100
        print("Model is successfully loaded!!!!!!")
        print(self.x1, self.y1, self.x2, self.y2)
        return image


    def predictimg(self, x):

        img = cv2.imread(x)
        box = self.load(img)

        self.download(box, self.x1, self.x2, self.y1,  self.y2)

        cv2.waitKey(0)
        cv2.destroyAllWindows()



