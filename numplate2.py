import numpy as np
import cv2 as cv
import easyocr

img = cv.imread('image2.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.bilateralFilter(gray, 11, 17, 17)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 100, 150)
cv.imshow('Canny', canny)

contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv.contourArea, reverse = True)[:10]
location = None
for contour in contours:
    approx = cv.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break
print(location)

blank = np.zeros(gray.shape, dtype = 'uint8')
cv.imshow('Blank', blank)
mask = cv.drawContours(blank, [location], 0, 255, -1)
cv.imshow('Mask', mask)
masked_image = cv.bitwise_and(img, img, mask = mask)
cv.imshow('Masked Image', masked_image)



cv.waitKey(0)

print('Done!')