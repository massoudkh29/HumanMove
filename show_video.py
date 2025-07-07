import cv2
import os

# Path to the video file
video_path = os.path.join(os.path.dirname(__file__), 'video1.mp4')

# Initialize HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Open the video file
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Could not open video {video_path}")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for faster processing and better detection
    frame_resized = cv2.resize(frame, (640, 360))

    # Detect people in the image
    boxes, weights = hog.detectMultiScale(frame_resized, winStride=(8,8))

    # Draw bounding boxes
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame_resized, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('HOG Person Detection', frame_resized)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 