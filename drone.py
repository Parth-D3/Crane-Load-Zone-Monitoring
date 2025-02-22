import cv2

gst_pipeline = (
    "v4l2src ! videoconvert ! video/x-raw,format=I420,width=640,height=480,framerate=30/1 ! "
    "x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! "
    "udpsink host= <enter_appro_ip_address> port=5000"
)


cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

print("Streaming video...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow("Drone Camera", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
