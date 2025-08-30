import cv2 as cv
import numpy as np
import pytesseract
import easyocr
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


carplate_image = cv.imread('image17.jpg')
carplate_haar_cascade = cv.CascadeClassifier(r'C:\Programming\Python\Number Plate Project\haarcascade_russian_plate_number.xml')

def numplate_coordinates(image):
    copy = image.copy()
    numplate_corners = carplate_haar_cascade.detectMultiScale(copy,scaleFactor=1.1, minNeighbors=5)
    print(numplate_corners)
    x,y,w,h = numplate_corners[0]
    coordinates = (x,y,x+w,y+h)
    print(coordinates)
    return coordinates

coordinates = numplate_coordinates(carplate_image)


def read_numplate(image, coordinates):
    xmin,ymin,xmax,ymax = coordinates
    box = image[int(ymin)-5:int(ymax)+5, int(xmin)-5:int(xmax)+5]
    cv.imshow("Box", box)

    gray = cv.cvtColor(box, cv.COLOR_RGB2GRAY)
    gray = cv.resize(gray, None, fx = 3, fy = 3, interpolation = cv.INTER_CUBIC)
    gray_blur = cv.GaussianBlur(gray, (5,5), 0)
    ret, thresh = cv.threshold(gray_blur, 0, 255, cv.THRESH_OTSU)
    #cv.imshow("OTSU", thresh)

    rect_kern = cv.getStructuringElement(cv.MORPH_RECT, (5,5))
    dilation = cv.dilate(thresh, rect_kern, iterations = 1)
    #cv.imshow("Dilation", dilation)

    contours, hierarchy = cv.findContours(dilation, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    sorted_contours = sorted(contours, key=lambda ctr: cv.boundingRect(ctr)[0])

    im2 = gray.copy()
    number_plate = ""

    for cnt in sorted_contours:
        x,y,w,h = cv.boundingRect(cnt)
        height, width = im2.shape
        if height/float(h) > 6:
            continue

        ratio = h/float(w)
        if ratio < 1.5:
            continue

        if width/float(w) > 15:
            continue

        area = h*w
        if area < 100:
            continue

        rect = cv.rectangle(im2, (x,y), (x+w, y+h), (0,255,0),2)
        roi = thresh[y-5:y+h+5, x-5:x+w+5]
        roi = cv.bitwise_not(roi)
        roi = cv.medianBlur(roi, 5)

        try:
            text = pytesseract.image_to_string(roi, config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8 --oem 3')
            clean_text = re.sub('[\W_]+', '', text)
            number_plate += clean_text
            #print(number_plate)
        except:
            text = None
    
    if text != None:
        print("License Plate:", number_plate)
    else:
        print("No license plate found! :(")

    cv.imshow("Character's Segmented", im2)
    cv.waitKey(0)

read_numplate(carplate_image, coordinates)

