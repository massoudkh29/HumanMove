import cv2
import os

# Path to the video file
video_path = os.path.join(os.path.dirname(__file__), 'video1.mp4')

# Open the video file
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Could not open video {video_path}")
    exit()

# Create background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Resize for faster processing
    frame_resized = cv2.resize(frame, (640, 360))
    # Apply background subtraction
    fgmask = fgbg.apply(frame_resized)
    # Threshold to get binary image
    _, fgmask_bin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
    # Find contours of moving objects
    contours, _ = cv2.findContours(fgmask_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw bounding boxes around moving objects
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:  # Filter small movements/noise
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame_resized, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow('Motion Detection', frame_resized)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 