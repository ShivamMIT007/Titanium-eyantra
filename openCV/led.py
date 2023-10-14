import cv2 as cv

# img = cv.imread('openCV/sample.jpg')

# cv.imshow('Sample', img)



def rescaleFrame(frame, scale=1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# resized_image = rescaleFrame(img)
# cv.imshow('Image', resized_image)
# cv.waitKey(0)
# def changeRes(width,height):
#     capture.set(6,width)
#     capture.set(1,height)
# Reading Videos

capture = cv.VideoCapture('cartoon.mp4')

while True:
    isTrue, frame = capture.read()

    # frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)

    # cv.imshow('Video', frame, scale=.2)
    # cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
