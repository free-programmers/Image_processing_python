OpenCV cv2 imread()
You can read image into a numpy array using opencv library. The array contains pixel level data. And as per the requirement, you may modify the data of the image at a pixel level by updating the array values.

To read an image in Python using OpenCV, use cv2.imread() function. imread() returns a 2D or 3D matrix based on the number of color channels present in the image. For a binary or grey scale image, 2D array is sufficient. But for a colored image, you need 3D array.



https://pythonexamples.org/python-opencv-read-image-cv2-imread/