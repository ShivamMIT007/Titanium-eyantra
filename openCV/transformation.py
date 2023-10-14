import cv2 as cv
import numpy as np

img = cv.imread('openCV/sphere.jpg')
cv.imshow('Sphere', img)

canny = cv.Canny(img, 125, 175)
cv.imshow('CannyEdges', canny)

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, -100, -100)
cv.imshow('Translate', translated)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotate', rotated)

rotated_rotated = rotate(rotated, 45)
cv.imshow('Rotated Rotated', rotated_rotated)

#Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Flipping
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

#cropping
cropped = img[400:800, 300:900]
cv.imshow('Cropped', cropped)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

contours, hieraschies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)