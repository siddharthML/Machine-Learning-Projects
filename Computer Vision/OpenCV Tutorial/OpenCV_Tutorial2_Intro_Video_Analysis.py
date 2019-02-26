# Code here didnt work very well. Corrupted file saved and video didnt
#turn grey

import cv2
import numpy as np

# Capture via system webcam

cap = cv2.VideoCapture(0)

#Save videos
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# How long to keep the video running
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #turn video feed gray

    cv2.imshow('frame', frame)
    cv2.imshow('gray', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# End feed before saving
cap.release()
out.release()
cv2.destroyAllWindows()