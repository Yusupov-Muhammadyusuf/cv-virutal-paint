# cv-virutal-paint

<img width="300" height="250" alt="paintbot" src="https://github.com/user-attachments/assets/48c2b49a-5496-4421-b30b-a570dc20635e" />

## Inspiration
The inspiration behind this project comes from the desire to create a **touchless interaction** experience. In an era where hygiene and digital innovation go hand in hand, "Virtual Paint" bridges the gap between physical movement and digital creativity. This project is inspired by futuristic sci-fi interfaces (like in *Iron Man*) where users can manipulate digital objects with simple hand gestures, making technology feel more natural and intuitive.

## Features
* **Real-time Drawing:** Draw on the screen using your index finger.
* **Selection Mode:** Use two fingers (index and middle) to select colors or pause drawing.
* **Color Palette:** Choose between Red, Green, and Blue.
* **Eraser:** A dedicated eraser mode to clean specific parts of your drawing.
* **Clear Canvas:** Press the **'c'** key to clear the entire screen.
* **Responsive UI:** Custom header for tool selection.

## Key Advantages
* **Zero Hardware Requirement:** No need for expensive drawing tablets or styluses—just your laptop camera.
* **Interactive Learning:** A great tool for kids or educators to engage in a fun, tech-driven creative process.
* **Low Latency:** Optimized with MediaPipe's latest Task API for smooth, lag-free drawing.
* **Hygiene & Accessibility:** Allows interaction without touching any surface, which is ideal for public displays or sterile environments.

## Important: Model File Required
To run this project, you need the **MediaPipe Hand Landmarker** model file. 

* **Download the model:** [hand_landmarker.task](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker#models)
* **Setup:** Place the downloaded file in the **root directory** of this project.
* **Reason:** This file is not included in the repository due to its size and to ensure you are always using the most up-to-date detection model.

## Tech Stack & Tools
This project is built using the following core technologies:

* **Python:** The primary programming language used for logic and integration.
* **OpenCV:** Used for real-time computer vision, video capturing, and image manipulation (drawing the canvas).
* **MediaPipe (Tasks API):** Google's high-level framework used specifically for the **Hand Landmarker** model to track 21 3D hand joints.
* **NumPy:** Used for high-performance matrix operations, especially for handling the drawing canvas and image overlays.
* **Math Logic:** Custom algorithms to calculate finger states (open/closed) and distance-based gesture recognition.
