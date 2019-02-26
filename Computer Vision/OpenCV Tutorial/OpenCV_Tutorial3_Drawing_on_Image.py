import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 15)  # Draw a white line

cv2.rectangle(img, (15,15), (200,150), (0, 255, 0), 5)  # Draw a rectangle

cv2.circle(img, (100,63), 55, (0,0,255), -1)  # -1 fills the whole circle up

font = cv2.FONT_HERSHEY_SIMPLEX  # Writing font.

cv2.putText(img, 'OpenCV Tuts', (0,130), font, 1, (200,255,255), 2, cv2.LINE_AA )
""" 

The color spectrum in opencv is BGR. If we wanted a purely blue image we would make our input
(255,0,0). Similarly red is (0,255,0) and blue is (0,0,255). Pure white is (255,255,255) and
pure black is (0,0,0).

"""

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

# WE can see a white line drawn in the image.
