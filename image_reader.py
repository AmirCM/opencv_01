import cv2 as cv

path = input('Insert image path\n')
cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
img = cv.imread(path, cv.IMREAD_COLOR)
cv.imshow('image', img)
k = cv.waitKey(0)

if ord('s'):
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite('gray_opencv.png', gray_img)
cv.destroyAllWindows()
