import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt

cap = cv.VideoCapture(1)
counter = 0
while cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    if ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    if counter > 1000:
        gray = cv.cvtColor(frame,cv.COLOR_BGRA2GRAY)
        cv.imshow('Webcam',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    counter += 1

cap.release()
cv.destroyAllWindows()