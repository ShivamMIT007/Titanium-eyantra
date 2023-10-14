import cv2 as cv

img = cv.imread('sample.jpg')

cv.imshow('sample', img)

cv.waitKey(0)