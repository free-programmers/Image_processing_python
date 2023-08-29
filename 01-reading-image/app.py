"""
by default open cv reads images in BGR mode BLUE, GREEN, RED
but otherlibraries cannot show this values properly like matplotlib
so its better to convert this values to BGR before showing it in other libraries

read about color spaces:
https://www.geeksforgeeks.org/color-spaces-in-opencv-python/

"""

import cv2 as cv


filename = "../Media/1.jpg" 

image = cv.imread(filename, 1) # filename: str, flags: int
# flags
# 1   0   -1

# convert BGR to RGB
image = cv.cvtColor(image, cv.COLOR_BGR2RGB) # src, code


# showing image with opencv
cv.imshow("Open Cv", image) # winname: str, mat: cv2.typing.MatLik


cv.waitKey(1000) # delay: int => milliseconds 
# if 0 is passed its wait until a key pressed on the keyboard

cv.destroyAllWindows() # remove all windows from memory


# showing images with mathplotlib
import matplotlib.pyplot as plt

plt.imshow(image)
plt.title("matplotlib")
plt.waitforbuttonpress()
plt.close('all')
