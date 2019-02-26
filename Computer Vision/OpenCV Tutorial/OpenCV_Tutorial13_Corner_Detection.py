import cv2
import numpy as np

# Finding corners depends a lot on image quality and aliasing of the image.
# A poor image will show unnecessarily large number of corners due to pixalation

img = cv2.imread('opencv-corner-detection-sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

# For some annoying reason the image window wont stay open without waitKey and destroyAllWindows
cv2.imshow('Corner', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
