import numpy as np
import cv2

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

#add = img1 + img2
# Both images retain their opaqueness and superimposed on each other

#add = cv2.add(img1, img2)
# We get a lot of white in this image. This version of add just added the pixel values together.
# This was to be expected as the maximum acceptable value of pixel is 255

weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
#The above weighted addition yields a better result than the non-weighted ones.

#cv2.imshow('add', add)
cv2.imshow('weighted', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ==========================================
# We will now superimpose the logo onto our image 1
# while making background more transparent for img2

import numpy as np
import cv2

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now we want to make a mask of the logo (gray scale)

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#We now set the threshold for the background where if they grey value is
# above 255 it will be converted to white

ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst


cv2.imshow('res', img1)
#cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
