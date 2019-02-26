import cv2
import numpy as np

# Detecting edges using the laplacian and sobel functions.

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # the underscore is used to ignore the values. If you don't want to use
    # specific values while unpacking, just assign that value to underscore(_).
    # Ignoring means assigning the values to special variable underscore(_).

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    # The sobel x is a horizontal gradient image whereas y is vertical gradient image.
    # Gradient here refers to the direction in which edges are detected in the video.
    # Gradients show us the directional intensity of the edges in video/image

    edges = cv2.Canny(frame, 100, 100)

    # The lower the threshold values, the more granier the edges are.
    # Too high thresholds can lead to no edges being detected at all.
    # Determine beforehand what object and what detail u want to be detecting at.

    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('edges', edges)



    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

