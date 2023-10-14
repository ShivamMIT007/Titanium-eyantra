import cv2 as cv

img = cv.imread('openCV/sample.jpg')

cv.imshow('Sample', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img,(9,9), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('CannyEdges', canny)

dilated = cv.dilate(canny, (3,3), iterations=5)
cv.imshow('Dilated', dilated)

eroded = cv.erode(dilated, (3,3), iterations =5)
cv.imshow('Eroded', eroded)

resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)

cropped = img[50:200, 400:600]
cv.imshow('Cropped', cropped)


cv.waitKey(0)