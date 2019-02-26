import cv2
import numpy as np

"""
 Reducing background in videos. The algorithm checks for changes in background in
 the previous frame and compares it to current frame and sees what has moved.
 Something which hasnt moved is now part of the background.
 
"""

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('fg', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()