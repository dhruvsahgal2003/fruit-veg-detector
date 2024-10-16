import os

os.environ['OPENCV_IO_ENABLE_JASPER'] = 'true'
os.environ['QT_QPA_PLATFORM'] = 'offscreen'

from ultralytics import YOLO
import cv2
import numpy as np

cv2.setNumThreads(0)
cv2.ocl.setUseOpenCL(False)


def detect_and_count(image_path):
    try:
        # Load the model
        model = YOLO('yolov8n.pt')  # make sure this path is correct

        # Read the image using OpenCV
        image_np = cv2.imread(image_path)
        if image_np is None:
            raise ValueError(f"Failed to read image from {image_path}")

        print(f"Image shape: {image_np.shape}")  # Debugging information

        # Perform detection
        results = model(image_np)

        # Process results
        class_counts = {}
        for r in results:
            for c in r.boxes.cls:
                class_name = model.names[int(c)]
                class_counts[class_name] = class_counts.get(class_name, 0) + 1

        return class_counts
    except Exception as e:
        print(f"Error in detect_and_count: {str(e)}")
        return {"error": str(e)}
