"""
with this method you can also do some color changes in images and then save it 
like instagram filters (grayscale, sepia, etc) 

"""

import cv2 as cv


filename = "../Media/1.jpg" 

image = cv.imread(filename, 1) # filename: str, flags: int
# flags
# 1   0   -1


result = cv.imwrite("./copy_file.jpg", image) # filename, img
print("Normal Copy: ",result)



image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
result = cv.imwrite("./copy_gray.jpg", image) # filename, img
print("Gray Copy: ",result)
