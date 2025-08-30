import numpy as np
import cv2 as cv
import easyocr

# import os
# os.environ['KMP_DUPLICATE_LIB_OK']='True'

img = cv.imread('image15.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)
blur = cv.bilateralFilter(gray, 11, 17, 17)
#cv.imshow('Blur', blur)
canny = cv.Canny(blur, 30, 200)
cv.imshow('Canny', canny)

contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv.contourArea, reverse = True)[:10]
location = None
for contour in contours:
    approx = cv.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break
#print(location)

blank = np.zeros(gray.shape, dtype = 'uint8')
#cv.imshow('Blank', blank)
mask = cv.drawContours(blank, [location], 0, 255, -1)
#cv.imshow('Mask', mask)
masked_image = cv.bitwise_and(img, img, mask = mask)
#cv.imshow('Masked Image', masked_image)

(x,y) = np.where(mask == 255)
(x1,y1) = (np.min(x), np.min(y))
(x2,y2) = (np.max(x), np.max(y))
num_plate = gray[x1:x2+1, y1:y2+1]
#cv.imshow('Number Plate', num_plate)

reader = easyocr.Reader(['en'])
result = reader.readtext(num_plate)
print(result)

text = result[0][-2]
print(text)
font = cv.FONT_HERSHEY_SIMPLEX
display = cv.putText(img, text=text, org=(approx[0][0][0], approx[1][0][1]+60,), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv.LINE_AA)
display = cv.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0), 3)
cv.imshow('Display', display)

cv.waitKey(0)

print('Done!')