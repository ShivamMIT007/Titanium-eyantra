import cv2 as cv

img = cv.imread('openCV/fruit.jpg')
cv.imshow('Fruit', img)

# resized = cv.resize(img, (900,500), interpolation = cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

#averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

#gaussian blur
gauss = cv.GaussianBlur(img,(3,3), 0)
cv.imshow('Gaussian Blur', gauss)

#median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

#bilateral blur
bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)