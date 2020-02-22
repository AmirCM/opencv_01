import cv2 as cv
import numpy as np

blank_img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('Image', cv.WINDOW_AUTOSIZE)
cv.imshow('Image', blank_img)
cv.waitKey(0)
