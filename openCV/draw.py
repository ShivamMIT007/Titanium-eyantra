import cv2  as cv
import numpy as np

# blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)
img = cv.imread('openCV/sample.jpg')
cv.imshow('Sample', img)

# img[200:300, 300:400] = 255,255,255
# cv.imshow('Green',img)


cv.rectangle(img, (300,300), (350,350), (0,400,0), 
thickness=1)
cv.imshow('Rectangle',img)

# cv.circle(img, (img.shape[1]//2, img.shape[0]//2), 50, (0,255,255), thickness=2)
cv.circle(img, (500,500), 50, (255,0,255), thickness=-1)
cv.imshow('Circle', img)

# cv.line(img, (100,250), (img.shape[1]//2, img.shape[0]//2), (255,255,255), thickness=3)
cv.line(img, (0,0), (300,400), (255,255,255), thickness=3)

#write  text
cv.putText(img, 'Hello My name is shivam', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', img)

cv.imshow('Line', img)
cv.waitKey(0)