import cv2 as cv
import numpy as np

bird_color = np.array([39,191,212])

#DETECTION IN IMAGE
img = cv.imread("bird.png")
height,width = np.shape(img)[0:-1]

#BIRD DETECTION
mask = cv.inRange(img,bird_color,bird_color)
print(np.shape(mask))
left_value = width
right_value = 0
upper_value = height
lower_value = 0

for j in range(width):
    for i in range(height):
        if mask[i][j] != 0:
            if left_value >= j:
                left_value = j
            if right_value <= j:
                right_value = j
            if upper_value >= i:
                upper_value = i
            if lower_value <= i:
                lower_value = i

print(left_value)
print(right_value)
print(upper_value)
print(lower_value)


cv.rectangle(img, (left_value, upper_value), (right_value, lower_value), color=(255,255,255), thickness=2)


cv.imshow("Bird",img)
cv.imshow("Mask",mask)
cv.waitKey(0)
