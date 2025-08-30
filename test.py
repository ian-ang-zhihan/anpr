import cv2 as cv
import numpy as np
import pytesseract
import easyocr


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


carplate_image = cv.imread('image15.jpg')
carplate_haar_cascade = cv.CascadeClassifier(r'C:\Programming\Python\Number Plate Project\haarcascade_russian_plate_number.xml')


def carplate_detect(image):
    carplate_overlay = image.copy()
    carplate_rects = carplate_haar_cascade.detectMultiScale(carplate_overlay,scaleFactor=1.1, minNeighbors=5)
    print(carplate_rects[0])

    for x,y,w,h in carplate_rects:
        cv.rectangle(carplate_overlay, (x,y), (x+w,y+h), (0,0,255), 5)

    return carplate_overlay


detected_carplate_img = carplate_detect(carplate_image)
cv.imshow('Carplate', detected_carplate_img)

"""
def carplate_extract(image):
    carplate_rects = carplate_haar_cascade.detectMultiScale(image,scaleFactor=1.1, minNeighbors=5)
    for x,y,w,h in carplate_rects: 
        carplate_img = image[y+15:y+h-10 ,x+15:x+w-20]
        
    return carplate_img


def enlarge_img(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_image = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    return resized_image


carplate_extract_img = carplate_extract(carplate_image)
carplate_extract_img = enlarge_img(carplate_extract_img, 150)
cv.imshow('Carplate Extract', carplate_extract_img)
carplate_extract_img_gray = cv.cvtColor(carplate_extract_img, cv.COLOR_BGR2GRAY)
carplate_extract_img_gray_threshold = cv.adaptiveThreshold(carplate_extract_img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Thresholded', carplate_extract_img_gray_threshold)
carplate_extract_img_gray_blur = cv.medianBlur(carplate_extract_img_gray,3)
carplate_extract_img_gray_blur_threshold = cv.adaptiveThreshold(carplate_extract_img_gray_blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
number_plate = pytesseract.image_to_string(carplate_extract_img_gray_blur_threshold, config = f'--psm 8 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
print("Pytesseract :", number_plate)


#---
reader = easyocr.Reader(['en'])
result = reader.readtext(carplate_extract_img_gray_blur_threshold)
print(result)


text = (result[0][-2]).replace(" ","").replace(".", "")
print("EasyOCR : ", text)
font = cv.FONT_HERSHEY_SIMPLEX
# display = cv.putText(carplate_img, text=text, org=(approx[0][0][0], approx[1][0][1]+60,), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv.LINE_AA)
# display = cv.rectangle(carplate_img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0), 3)
#cv.imshow('Display', display)
"""
cv.waitKey(0)

