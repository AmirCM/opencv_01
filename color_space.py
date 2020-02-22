import cv2 as cv
from matplotlib import pyplot as plt

indoor = cv.imread('indoor.png', cv.IMREAD_COLOR)
outdoor = cv.imread('outdoor.png', cv.IMREAD_COLOR)
indoor_hsv = cv.cvtColor(indoor, cv.COLOR_BGR2HSV)
outdoor_hsv = cv.cvtColor(outdoor, cv.COLOR_BGR2HSV)
inh, ins, inv = cv.split(indoor_hsv)
oh, os, ov = cv.split(outdoor_hsv)

plt.subplot(241), plt.imshow(indoor), plt.title('Indoor')
plt.subplot(242), plt.imshow(inh), plt.title('H')
plt.subplot(243), plt.imshow(ins), plt.title('S')
plt.subplot(244), plt.imshow(inv), plt.title('V')

plt.subplot(245), plt.imshow(outdoor), plt.title('Outdoor')
plt.subplot(246), plt.imshow(oh), plt.title('H')
plt.subplot(247), plt.imshow(os), plt.title('S')
plt.subplot(248), plt.imshow(ov), plt.title('V')

plt.show()
