import cv2 as cv
import numpy as np

blank_img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('Image', cv.WINDOW_AUTOSIZE)

cv.line(blank_img, (0, 0), (511, 511), (250, 100, 0), 10)
cv.rectangle(blank_img, (384, 0), (510, 128), (0, 255, 0), 3)
cv.circle(blank_img, (447, 63), 63, (0, 0, 255), -1)
cv.ellipse(blank_img, (256, 256), (100, 20), 0, 0, 360, (0, 255, 0), 5)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(blank_img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)

cv.imshow('Image', blank_img)
cv.waitKey(0)
