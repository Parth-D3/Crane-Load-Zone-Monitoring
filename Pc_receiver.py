import cv2

gst_pipeline = (
    "udpsrc port=5000 caps=\"application/x-rtp\" ! "
    "rtph264depay ! avdec_h264 ! videoconvert ! appsink"
)

cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

print("Receiving video...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: No frame received.")
        break

    cv2.imshow("Drone Live Feed", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
