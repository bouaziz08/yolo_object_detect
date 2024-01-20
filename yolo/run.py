import math
import os
from ultralytics import YOLO
import cv2
import cvzone

URL = "0_12.jpg"


classNames = ["laptop"]
#
# cap = cv2.VideoCapture(URL)
# ret, frame = cap.read()
model_path = os.path.join('.', 'runs', 'detect', 'train9', 'weights', 'best.pt')
model = YOLO(model_path)
# while True:
    # Capture frame-by-frame
# ret, frame = cap.read()
resultat = model('opencv_frame_1.jpg', show=True)
cv2.waitKey(0)
#     for r in resultat:
#         boxes = r.boxes
#         for box in boxes:
#             x1, y1, x2, y2 = box.xyxy[0]
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#             print(x1, y1, x2, y2)
#             #
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)
#             w, h = x2 - x1, y2 - y1
#             cvzone.cornerRect(frame, (x1, y1, w, h))
#             #
#             conf = math.ceil((box.conf[0]*100))/100
#             cls = int(box.cls[0])
#             cvzone.putTextRect(frame, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)))
#
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break
#
#
# cap.release()
# cv2.destroyAllWindows()

# def runner():
#
#     VIDEOS_DIR = os.path.join('.', 'videos')
#
#     video_path = os.path.join(VIDEOS_DIR, 'laptop.mp4')
#     video_path_out = '{}_out.mp4'.format(video_path)
#
#     cap = cv2.VideoCapture(video_path)
#     ret, frame = cap.read()
#     H, W, _ = frame.shape
#     out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))
#
#     model_path = os.path.join('.', 'runs', 'detect', 'train9', 'weights', 'best.pt')
#
#     # Load a model
#     model = YOLO(model_path)  # load a custom model
#
#     threshold = 0.5
#
#     while ret:
#
#         results = model(frame)[0]
#
#         for result in results.boxes.data.tolist():
#             x1, y1, x2, y2, score, class_id = result
#
#             if score > threshold:
#                 cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
#                 cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
#                             cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
#
#         out.write(frame)
#         ret, frame = cap.read()
#
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()
#
#
# runner()

# import torch
#
# if torch.cuda.is_available():
#     d = "cuda.0"
# else:
#     d = "cpu"
#
# print(d)