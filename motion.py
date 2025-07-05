import cv2
import os
import datetime

# === Create a folder on Desktop named 'detection' ===
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
detection_folder = os.path.join(desktop_path, "detection")
os.makedirs(detection_folder, exist_ok=True)

# === Load pre-trained human detector model (HOG + SVM) ===
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# === Start Webcam ===
cap = cv2.VideoCapture(0)

# === Initialize for motion detection ===
ret, frame1 = cap.read()
ret, frame2 = cap.read()

print("[INFO] Starting detection... Press 'q' to quit.")

while cap.isOpened():
    # === Compute frame difference for motion detection ===
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            motion_detected = True
            break

    # === If motion detected, check for humans ===
    if motion_detected:
        gray_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        boxes, weights = hog.detectMultiScale(gray_frame, winStride=(8, 8))

        if len(boxes) > 0:
            # Save image
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join(detection_folder, f"detection_{timestamp}.jpg")
            cv2.imwrite(filename, frame1)
            print(f"[INFO] Human detected! Image saved: {filename}")

            # Draw rectangles for visualization (optional)
            for (x, y, w, h) in boxes:
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show live video (optional)
    cv2.imshow("Live Feed", frame1)

    # Update frames
    frame1 = frame2
    ret, frame2 = cap.read()

    if not ret or cv2.waitKey(10) & 0xFF == ord('q'):
        break

# === Release resources ===
cap.release()
cv2.destroyAllWindows()
print("[INFO] Detection stopped.")
