import numpy as np
import cv2 as cv 
import easyocr

platecascade = cv.CascadeClassifier(r'C:\Programming\Python\Number Plate Project\haarcascade_russian_plate_number.xml')
minArea = 500 
count = 0 

cap = cv.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    #flip = cv.flip(frame, 1)
    # img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # numberplates = platecascade.detectMultiScale(img_gray, 1.1, 4)
    # for (x,y,w,h) in numberplates:
    #     area = w * h
    #     if area > minArea:
    #         cv.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
    #         cv.putText(frame, "NUMBER PLATE", (x,y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    #         number_plate = frame[x:x+w+500, y:y+h+500]
    #         cv.imshow("Number Plate", number_plate)
    cv.imshow('Frame', frame)

    # reader = easyocr.Reader(['en'])
    # result = reader.readtext(number_plate)
    # print(result)
    # text = result[0][-2]
    # print(text)

    filepath = r'C:\Programming\Python\Number Plate Project\image17.jpg'
    if cv.waitKey(1) & 0xFF == ord('w'):
        cv.imwrite(filepath, frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
cv.waitKey(1000)

img = cv.imread('image17.jpg')
cv.imshow('Image', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

cv.waitKey(0)

# if cv.waitKey(1) & 0xFF == ord('e'):
#     cv.destroyAllWindows()

# reader = easyocr.Reader(['en'])
# result = reader.readtext(number_plate)
# print(result)
# text = result[0][-2]
# print(text)