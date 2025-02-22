import streamlit as st
import cv2
import tempfile
import numpy as np
import os
from inference_sdk import InferenceHTTPClient
from dotenv import load_dotenv

load_dotenv()

CLIENT = InferenceHTTPClient(
    api_url=os.getenv("ROBOFLOW_API_URL"),
    api_key=os.getenv("ROBOFLOW_API_KEY")
)

st.title("🔍 Person Detection in Large Video Files 🎥")

uploaded_file = st.file_uploader("Upload a video (max 1GB)", type=["mp4", "avi", "mov"])

if uploaded_file:
    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_video.write(uploaded_file.read())
    temp_video.close()

    cap = cv2.VideoCapture(temp_video.name)
    
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4").name
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    st.write("Processing video... ⏳")
    progress_bar = st.progress(0)

    frame_skip = max(1, total_frames // 500)
    processed_frames = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frames += 1
        if processed_frames % frame_skip != 0:
            continue

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = CLIENT.infer(frame_rgb, model_id="person-detection-9a6mk/16")

        for prediction in result.get('predictions', []):
            x, y, w, h = int(prediction['x']), int(prediction['y']), int(prediction['width']), int(prediction['height'])
            x1, y1, x2, y2 = x - w // 2, y - h // 2, x + w // 2, y + h // 2
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, "Person", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        out.write(frame)
        progress_bar.progress(min(processed_frames / total_frames, 1.0))

    cap.release()
    out.release()

    st.success("✅ Processing Complete!")
    st.video(output_path)

    with open(output_path, "rb") as file:
        st.download_button("⬇️ Download Processed Video", file, file_name="output.mp4")
