from ultralytics import YOLO
import cv2
import os

def detect_and_count(image_path):

    model = YOLO('src/yolov8n.pt')  # Adjust this path if needed


    results = model(image_path)


    detections = results[0].boxes.data.tolist()
    classes = results[0].names


    class_counts = {}
    for detection in detections:
        class_id = int(detection[5])
        class_name = classes[class_id]
        if class_name in class_counts:
            class_counts[class_name] += 1
        else:
            class_counts[class_name] = 1


    img = cv2.imread(image_path)
    for detection in detections:
        x1, y1, x2, y2, conf, class_id = detection
        class_name = classes[int(class_id)]
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(img, f"{class_name}: {conf:.2f}", (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


    output_path = f"output_{os.path.basename(image_path)}"
    cv2.imwrite(output_path, img)
    print(f"Annotated image saved as {output_path}")


    cv2.imshow("Detections", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return class_counts

if __name__ == "__main__":
    test_image_path = "/Users/dhruvsahgal/fruit_veg_detector/data/fruits_vegetables_detection_dataset/test/images/2024-03-21_17-22-49-346687_jpg.rf.235e8e7d016af05a1c4e7c814003ac57.jpg"
    results = detect_and_count(test_image_path)
    print(results)