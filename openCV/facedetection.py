import cv2 as cv


img = cv.imread("C:\\Users\\C36\\Desktop\\openCV\\group2.jpg")
cv.imshow('Group2', img)          # shows the real image

resized = cv.resize(img, (1000,1000), interpolation = cv.INTER_CUBIC)
# cv.imshow('Resized', resized)  #  shows the resized image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Chris', gray)    #shows the gray image



haar_cascade = cv.CascadeClassifier("C:\\Users\\C36\Desktop\\openCV\\haar_face.xml")
# haar_cascade = cv.CascadeClassifier("C:\\Users\C36\\Desktop\\openCV\\fruit.jpg")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(f'Number of faces found = {len(faces_rect)}')


for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)


for i, rectangle in enumerate(faces_rect):
    cv.putText(img, "+"+ str(len(faces_rect)),(x-10,y-10),cv.FONT_HERSHEY_COMPLEX, .5, (0,255,0), 2)
# cv.imshow('Put Text', img)
for i, rectangle in enumerate(faces_rect):
    cv.putText(img, "+"+ str(len(faces_rect)),(x-20,y-20),cv.FONT_HERSHEY_COMPLEX, .5, (0,255,0), 2)
# cv.imshow('Put Text', img)

cv.imshow('Detected Faces', img)

cv.waitKey(0)