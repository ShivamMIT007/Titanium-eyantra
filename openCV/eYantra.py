import cv2 as cv
import numpy as np

img = cv.imread('openCV/sample.jpg')
cv.imshow('Sample', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 155, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("Number of LED = " + str(len(contours)))

cv.drawContours(img, contours, -1, (0, 255, 0), 2, lineType=cv.LINE_AA)
cv.imshow('Draw Contours', img)


led_info = []

for contour in contours:
    area = cv.contourArea(contour)


    M = cv.moments(contour)
    if M["m00"]!= 0:
            cx = float(M["m10"]/M["m00"])
            cy = float(M["m01"]/M["m00"])
            led_info.append({'centroid': (cx,cy), 'area:': area })

for i, led in enumerate(led_info):
    print(f"LED {i+1}: Centroid {led['centroid']}")
    print(f"Contour Area: {area}")

x,y,w,h = cv.boundingRect(contour)
cv.putText(img, "+"+ str(len(contours)),(x-10,y-10),cv.FONT_HERSHEY_COMPLEX, .5, 
(0,255,0), 2)

# # cv.imwrite('led_detection_result.jpg', img)
cv.imshow('Put Text', img)

cv.waitKey(0)
cv.destroyAllWindows()