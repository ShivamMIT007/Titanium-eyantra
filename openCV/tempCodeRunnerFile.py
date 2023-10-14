resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)