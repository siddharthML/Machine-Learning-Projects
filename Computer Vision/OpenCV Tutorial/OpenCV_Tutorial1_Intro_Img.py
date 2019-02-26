import cv2
import matplotlib.pyplot as plt
import numpy as np

# Simplify image to grayscale:

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)

"""
Note that in case of CV2 the channels are BGR and not RGB.
Converting to grayscale ensures we are dealing with just 1 colour channel.

"""



cv2.imshow('image', img) # plot the image
cv2.waitKey(0) # destroy the image if a key is pressed
cv2.destroyAllWindows()



# Plotting with matploblib

#plt.imshow(img, cmap= 'gray', interpolation="bicubic")
#plt.plot([50,100], [80,100], 'c', linewidth = 5) #directly plotting a line on img
#plt.show()

# Matplob inputs are indexed RGB and not BGR like cv2

"To save an image we can use the following command"

cv2.imwrite('watchgray.png', img)
