import cv2
import os

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

while True:
    success, img = cap.read()
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    cv2.imshow("Image", img)
    cv2.imshow("Slide", imgCurrent)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break