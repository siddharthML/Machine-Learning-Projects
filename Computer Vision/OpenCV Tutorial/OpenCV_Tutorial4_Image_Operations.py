import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

"""
Input source is full color. Then it is converted to gray scale. And a rectangle is drawn on the object in gray scale.

"""

# To find color value for particular pixel

px = img[55,55]
print(px)

# To modify a pixel

img[55,55] = [255,255,255]


#watch_face = img[25:50, 76:99]
#img[0:30, 0:25] = watch_face

print(px)

# Region of Image (ROI)

roi = img[100:150, 100:150] = [255, 255, 255]

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
