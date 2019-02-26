import cv2
import numpy as np
import matplotlib.pyplot as plt

# Here we will try and extract features from completely different templates.
# Template changes can be based on image orientation, lighting etc.
# The match is being done through brute force rather than anything intelligent seen in ML.

img1 = cv2.imread('opencv-feature-matching-template.jpg', 0)
img2 = cv2.imread('opencv-feature-matching-image.jpg', 0)
# The 0 is just changing channel color. If we changed to 1 the image would be in blue.


orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2. BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags = 2)

# 10 specifies number of matches we want.
# If we increase this number to be too great then the program starts to make
# spurious matches.

plt.imshow(img3)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
We can see the matches are made side by side using lines cateogrizing things like
head, tail, stone etc of the honey badger despite the changed orientation of two
images.

"""