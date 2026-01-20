import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
img = cv.imread("Bird/bird_only.jpg")
img2 = cv.imread("Bird/bird_only_2.jpg")
cv.imshow("Bird",img)
orb = cv.ORB_create()

kp1, des1 = orb.detectAndCompute(img,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv.BFMatcher()

matches = bf.knnMatch(des1,des2,k=2)

good = []

for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

img3 = cv.drawMatchesKnn(img,kp1,img2,kp2,good,None,flags=2)

cv.imshow("img3",img3)
cv.waitKey(0)

