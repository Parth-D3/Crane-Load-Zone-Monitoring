import cv2
from ultralytics import YOLO
import tempfile
import os

model = YOLO(r"models\person.pt")
def process_image(image):
    results = model.predict(image, conf=0.5)
    
    # Convert PIL Image to OpenCV format
    image_cv = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    # Draw detections
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls_id = int(box.cls[0])
            
            if model.names[cls_id] == 'person':
                # Draw bounding box
                cv2.rectangle(image_cv, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f'person {conf:.2f}'
                cv2.putText(image_cv, label, (x1, y1-10), 
                           cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
    
    return cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)

img = "person1.jpg"
image = cv2.imread(img)
processed_image = process_image(image)
cv2.imwrite("output.jpg",processed_image)

