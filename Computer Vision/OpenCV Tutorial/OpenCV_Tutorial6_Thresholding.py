import cv2
import numpy as np

# Thresholding: Extreme minimizing/maximizing of pixels into black or white.

img = cv2.imread('bookpage.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
# Our new minimum value is 12, and maximum value is 255
# We have made our dark blurry image much brighter using the manipulations above.


graysclaed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
reval2, threshold2 = cv2.threshold(graysclaed, 12, 255, cv2.THRESH_BINARY)

# Above converts image to black and white making the dark spots
# almost impossible to read.


# We will now make an (Gaussian) adaptive threshold:

gaus = cv2.adaptiveThreshold(graysclaed, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# The adaptive Gaussian does an excellent job cleaning up the black and white images based on its
# position with shadow area.

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()