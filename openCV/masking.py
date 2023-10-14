import cv2 as cv
import numpy as np

img = cv.imread('openCV/fruit.jpg')
cv.imshow('Fruit', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2) ,255,-1)
# cv.imshow('Mask',mask)

mask = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2),100 ,255,-1)
cv.imshow('Mask',mask)

rectangle = cv.rectangle(blank.copy(), (30,30), (360,380), 255, -1 )
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)


weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weired Shape', weird_shape)

masked = cv.bitwise_and(img,img,mask= weird_shape)
cv.imshow('Wierd Shaped Masked Image', masked)



cv.waitKey(0)