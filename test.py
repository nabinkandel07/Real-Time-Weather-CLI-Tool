from ultralytics import YOLO
import os
import sys
import torch 

# Load a pre-trained YOLOv8 model
model = YOLO('yolo11n.pt')

# Train the model using the dataset configuration from the YAML file
results = model.train(
    data='data.yaml',
    epochs=10,
    imgsz=640, hsv_h=0.03, hsv_s=0.6, hsv_v=0.5
)
