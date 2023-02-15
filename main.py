import cv2
import os
from cvzone.HandTrackingModule import HandDetector

# Variables
# Similar to presentation, but need not be
width, height = 1280, 720
folderPath = "Presentation"

# Camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

#List of Presentation Images
pathImages = sorted(os.listdir(folderPath), key = len)

# Change Slide Number
imgNumber = 0
hs, ws = 120, 210

# Hand Detector
detector = HandDetector(detectionCon = 0.85, maxHands = 1)


while True:
    success, img = cap.read()
    # Flip Image horizontally
    img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        # Check fingers up
        fingers = detector.fingersUp(hand)
        print(fingers)

    # Adding WebCam on slides
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w-ws:w] = imgSmall

    cv2.imshow("Image", img)
    cv2.imshow("Slide", imgCurrent)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break