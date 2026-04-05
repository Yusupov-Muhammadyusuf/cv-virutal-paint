# cv-virutal-paint

## Virtual Paint using MediaPipe 🎨

This is a computer vision-based application that allows users to draw in the air using hand gestures. It uses **OpenCV** for image processing and **MediaPipe** for high-performance hand landmark detection.

## 🚀 Features
* **Real-time Drawing:** Draw on the screen using your index finger.
* **Selection Mode:** Use two fingers (index and middle) to select colors or pause drawing.
* **Color Palette:** Choose between Red, Green, and Blue.
* **Eraser:** A dedicated eraser mode to clean specific parts of your drawing.
* **Clear Canvas:** Press the **'c'** key to clear the entire screen.
* **Responsive UI:** Custom header for tool selection.

## ⚠️ Important: Model File Required

To run this project, you need the **MediaPipe Hand Landmarker** model file. 

1. Download the model: **`hand_landmarker.task`**
2. You can get it from the [Official MediaPipe Documentation](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker#models).
3. Place the downloaded file in the **root directory** of this project.

> **Note:** This file is not included in the repository due to its size and to ensure you use the latest version.
