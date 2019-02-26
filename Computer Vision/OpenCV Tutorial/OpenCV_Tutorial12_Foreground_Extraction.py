import cv2
import numpy as np
import matplotlib.pyplot as plt



img = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')

mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

# Code for most images is the same other than where to place the rectangle:

rect = (161, 79, 150, 150)

# We will now use grabcut to grab and cut a certain region.

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')

img = img*mask2[: , : ,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()