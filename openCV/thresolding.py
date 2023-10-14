import cv2 as cv

img = cv.imread('openCV/sphere.jpg')
cv.imshow('Sphere', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#simple
threshold, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

#adoptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
cv.THRESH_BINARY_INV, 15, 9)
cv.imshow('Adaptive thresholding', adaptive_thresh)

cv.waitKey(0)