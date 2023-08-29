import cv2 as cv


filename1 = "../Media/1.jpg"
filename2 = "../Media/2.jpg"

file1 = cv.imread(filename1)
file2 = cv.imread(filename2)


file1 = cv.resize(file1, (600,600))
cv.imshow("file 1", file1)
cv.waitKey(1000)


file2 = cv.resize(file2, (600,600))
cv.imshow("file 2", file2)
cv.waitKey(1000)




file = cv.addWeighted(file1, 0.5, file2, 0.5, 0) # src1: UMat, alpha: float, src2: UMat, beta: float, gamma: float, dst: UMat | None = ..., dtype: int = ...)

cv.imshow("result", file)
cv.waitKey(0)
cv.destroyAllWindows()