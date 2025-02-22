import cv2
import torch
from ultralytics import YOLO
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

def draw_detection(frame, box, color):
    """Helper function to draw bounding boxes and labels inside the box."""
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    confidence = box.conf[0].item()

   
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

    
    label_text = f"Vehicle {confidence:.2f}"
    label_size = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]

    text_x = x1 + 5  
    text_y = y2 - 5  

   
    cv2.rectangle(frame, (x1, y2 - label_size[1] - 10), (x1 + label_size[0] + 5, y2), color, -1)

  
    cv2.putText(frame, label_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

def process_and_save_video(truck_model_path, vehicle_model_path, video_path, output_path):
    """Process video with both YOLO models and save to file"""

    truck_model = YOLO(truck_model_path)
    vehicle_model = YOLO(vehicle_model_path)
    
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    truck_model.to(device)
    vehicle_model.to(device)
    print(f"Using device: {device}")
    
   
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("Error: Could not open video.")
    

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
   
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
 
    vehicle_color = (0, 255, 0)  

    try:
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                print("End of video stream")
                break

        
            truck_results = truck_model(frame)
            vehicle_results = vehicle_model(frame)

            
            for result in truck_results:
                for box in result.boxes:
                    draw_detection(frame, box, vehicle_color)

            for result in vehicle_results:
                for box in result.boxes:
                    draw_detection(frame, box, vehicle_color)

            
            out.write(frame)
            
           
            frame_count += 1
            if frame_count % 30 == 0:  
                progress = (frame_count / total_frames) * 100
                print(f"Processing: {progress:.1f}% complete")

    finally:
        cap.release()
        out.release()
        print(f"Processing complete. Output saved to: {output_path}")

if __name__ == "__main__":

    # update required paths
    TRUCK_MODEL_PATH = ""
    VEHICLE_MODEL_PATH = ""
    VIDEO_PATH = ""
    OUTPUT_PATH = ""
    try:
        process_and_save_video(TRUCK_MODEL_PATH, VEHICLE_MODEL_PATH, VIDEO_PATH, OUTPUT_PATH)
    except Exception as e:
        print(f"An error occurred: {str(e)}")