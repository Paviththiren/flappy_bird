import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame,cv.COLOR_BGRA2GRAY)
    cv.imshow('Webcam',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()