import cv2 as cv
import numpy as np
import math
# cap=cv.VideoCapture(1)
frame=cv.imread('image/side/side_0.jpg')
hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
hsv=hsv[:,:,1]
cv.imshow('a',hsv)
cv.waitKey(0)
# cap.set(15, .000001)
