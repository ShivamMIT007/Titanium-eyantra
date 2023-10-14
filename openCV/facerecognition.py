import cv2 as cv
import numpy as np
import os

img = cv.imread('openCV/chris.jpg')
cv.imshow('Chris', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Chris', gray)

haar_cascade = cv.CascadeClassifier('C:\\Users\\C36\\Desktop\\openCV\\haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

cv.waitKey(0)