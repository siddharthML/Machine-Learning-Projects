import cv2
import numpy as np

# Add, remove or show a specific color range. Here we will filter for red color.

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    #hsv hue sat value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # changing the first element of following array helps remove the background.
    # More the value, greater is background removal

    lower_red = np.array([150,150,50])
    upper_red = np.array([180, 255, 150])

    # dark_red = np.units([[[12, 22, 121]]])
    # dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)


    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    """
    The mask is a boolean operation. So either the pixel is in the range we have
    defined or it isn't. 
    
    """

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()