import cv2
import numpy as np

# There are two types of morphological transformations : erosion and dilation.
# Erosion is a slider that slides around the pictures and ensures that there is
# regional heterogeneity through the image.
# Dilation does the opposite and highlights color difference within regions.


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # hsv hue sat value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # changing the first element of following array helps remove the background.
    # More the value, greater is background removal

    lower_red = np.array([150, 150, 50])
    upper_red = np.array([180, 255, 150])

    # dark_red = np.units([[[12, 22, 121]]])
    # dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)

    # Opening and Closing:
    # Opening: remove stuff from background that are false positives.
    # Closing: removes false negatives.

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernel)



    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('dilation', dilation)

    # Tophat: it is difference between input image and Opening of the image
    cv2.imshow('Tophat', tophat)

    # Blackhat: it is difference between closing of the input image and input image
    cv2.imshow('Blackhat', blackhat)




    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()