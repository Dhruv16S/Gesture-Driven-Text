import cv2

# Variables
# Similar to presentation, but need not be
width, height = 1280, 720


# Camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

while True:
    succes, img = cap.read()
    


    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break