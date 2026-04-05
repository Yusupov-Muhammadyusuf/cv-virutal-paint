import cv2 as cv
import mediapipe as mp
import numpy as np

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands = 2,
    min_hand_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
)

detector = vision.HandLandmarker.create_from_options(options)

HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),       
    (0, 5), (5, 6), (6, 7), (7, 8), 
    (0, 9), (9, 10), (10, 11), (11, 12),  
    (0, 13), (13, 14), (14, 15), (15, 16), 
    (0, 17), (17, 18), (18, 19), (19, 20),
    (5, 9), (9, 13), (13, 17),
]

header = cv.imread("PaintDesign.png")

cap = cv.VideoCapture(0)

canvas = None
xp, yp = 0, 0

# cv.namedWindow("Virtual Paint", cv.WINDOW_NORMAL)
drawColor = (0, 255, 0)

while True:
    ret, frame = cap.read()
    h, w, c = frame.shape
#
    header_resize = cv.resize(header, (w, 100))

    if canvas is None:
        canvas = np.zeros((h, w, 3), dtype="uint8")

    frame = cv.flip(frame, 1)
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    result = detector.detect(mp_image)

    if result.hand_landmarks:
        for hand_landmarks in result.hand_landmarks:
            points = []

            for landmark in hand_landmarks:
                points.append((int(landmark.x * w), int(landmark.y * h)))

            x1, y1 = points[8]
            x2, y2 = points[12]

            index_open = points[8][1] < points[6][1]
            middle_open = points[12][1] < points[10][1]

            if index_open and middle_open:
                xp, yp = 0, 0

                if y1 < 100:
                    if 150 < x1 < 230:
                        drawColor = (255, 0, 0)
                    elif 260 < x1 < 360:
                        drawColor = (0, 255, 0)
                    elif 410 < x1 < 470:
                        drawColor = (0, 0, 255)
                    elif 520 < x1 < w:
                        drawColor = (0, 0, 0)
                        
                cv.circle(frame, (x1, y1), 10, drawColor, cv.FILLED)
                cv.putText(frame, "Pause", (50, 50), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
            elif index_open and not middle_open:
                dot_size = 20 if drawColor == (0, 0, 0) else 5

                cv.circle(frame, (x1, y1), dot_size, drawColor, cv.FILLED)

                if xp == 0 and yp == 0:
                    xp, yp = x1, y1

                thickness = 50 if drawColor == (0, 0, 0) else 10
                cv.line(canvas, (xp, yp), (x1, y1), drawColor, thickness)
                xp, yp = x1, y1
            else:
                xp, yp = 0, 0

    img_gray = cv.cvtColor(canvas, cv.COLOR_BGR2GRAY)
    _, img_inv = cv.threshold(img_gray, 20, 255, cv.THRESH_BINARY_INV)
    img_inv = cv.cvtColor(img_inv, cv.COLOR_GRAY2BGR)

    frame = cv.bitwise_and(frame, img_inv)
    frame = cv.bitwise_or(frame, canvas)

    frame[0:100, 0:w] = header_resize

    cv.imshow("Virtual Paint", frame)

    key = cv.waitKey(1) & 0xFF
    if key == ord("q"): 
        break
    
    if key == ord("c"):
        canvas = np.zeros((h, w, 3), np.uint8)

cap.release()
cv.destroyAllWindows()