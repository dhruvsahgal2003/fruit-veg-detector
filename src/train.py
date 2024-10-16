from ultralytics import YOLO

def train_model():

    model = YOLO('yolov8n.pt')


    results = model.train(
        data='data/fruits_vegetables_detection_dataset/data.yaml',  # Updated path
        epochs=100,
        imgsz=640,
        batch=16,
        name='fruit_veg_model'
    )

    print(results)

if __name__ == "__main__":
    train_model()