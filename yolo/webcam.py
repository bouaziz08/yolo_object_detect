
#####################################################################
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

# Train the model
resultat = model.train(data='config.yaml', epochs=100)
