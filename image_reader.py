import cv2 as cv

path = input('Insert image path\n')
img = cv.imread(path, cv.IMREAD_COLOR)
cv.imshow('img', img)
cv.waitKey(0)
