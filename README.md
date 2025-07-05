# Motion & Human Detection using OpenCV

This Python project uses OpenCV to detect **motion** and identify **humans** in real-time using a webcam. When a human is detected, it saves the image to a folder on your desktop.

---

## 📸 Features

- Detects motion by comparing consecutive frames.
- Applies a pre-trained HOG + SVM model for human detection.
- Saves a snapshot of the frame when a human is detected.
- Stores images in a folder named `detection` on your desktop.
- Real-time webcam feed display.
- Press `q` to stop detection.

---

## 🚀 Requirements

- Python 3.x
- OpenCV

Install dependencies:
```bash
pip install opencv-python
