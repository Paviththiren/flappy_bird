import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)
img = cv.imread("Bird/bird_only.jpg")
img_w = img.shape[1]
img_h = img.shape[0]
cv.imshow("Bird",img)
threshold = 0.5

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    result = cv.matchTemplate(frame,img,cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    if max_val > threshold:
        top_left = max_loc
        bottom_right = (top_left[0] + img_w, top_left[1] + img_h)
        cv.rectangle(frame,top_left, bottom_right,color=(255,255,255),thickness=3, lineType=cv.LINE_4)
    cv.imshow('Webcam',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
        break


cap.release()
cv.destroyAllWindows()
cv.waitKey()