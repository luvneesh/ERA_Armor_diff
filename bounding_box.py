import cv2 as cv
import numpy as np
import math
cap=cv.VideoCapture(0)
cap.set(15, .000001)
while True :
    ret,frame=cap.read()
    
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    mask=cv.inRange(hsv,np.array([90,150,150]),np.array([150,255,255]))
    final=cv.bitwise_and(frame,frame,mask=mask)
    gray=cv.cvtColor(final,cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(final, contours, -1, (0,255,0), 3)
    hset=[]
    filters=np.ones(final.shape[:2],dtype="uint8")*255
    for i in contours:
        x,y,w,h = cv.boundingRect(i)
        if w/h<0.000000000005:
            cv.rectangle(final,(x,y),(x+w,y+h),(255,0,0),2)
            cv.drawContours(filters,[i],-1,1,2)
            # hset.append(h)
    # cv.imshow('d',frame)
    # cv.imshow('c',filters)
    # print(hset)      
    image=cv.bitwise_and(frame,frame,mask=cv.bitwise_not(filters))  
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    
    ret, thresh = cv.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    rectangles=[]
    max_rect=[]
    bgr=cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
    max_area=0
    ind_max=0
    for j,i in enumerate(contours):
        rect= cv.minAreaRect(i)
        w, h=rect[1]
        rectangles.append(rect)
        area = h*w
        if(area > max_area):
            # max_rect.clear()
            ind_max=j
            max_area=area
            # max_rect.append(rect)
    try:
        var = 0
        interest=[]
        # print(ind_max)
        interest.append(ind_max)
        if ind_max==0:
            interest.append(1)
        elif ind_max==(len(rectangles)-1):
            interest.append(len(rectangles)-2)
        else :
            
            rect1=rectangles[ind_max-1]
            rect2=rectangles[ind_max+1]
            rect0=rectangles[ind_max]
            angle_i=rect1[2]
            angle_j=rect2[2]
            angle_k=rect0[2]
            diff1=abs(angle_k-angle_j)
            diff2=abs(angle_k-angle_i)
            if diff1<diff2:
                interest.append(ind_max+1)
            else:
                interest.append(ind_max-1)
            # if(difference)
        for j in interest:
                    
            # w, h=rect[1]
            # area = h*w
            rect=rectangles[j]
            box = cv.boxPoints(rect)
            box = np.int0(box)
            cv.drawContours(frame, [box], 0, (0,0,255),2)
            # rectangles.append(rect)
        
        rect=rectangles[interest[0]]
        rectangle=rectangles[interest[1]]
        angle_i=rect[2]
        angle_j=rectangle[2]
        x1,y1=rect[0]
        x2,y2=rectangle[0]
        x=int ((x1+x2)/2)
        y=int ((y1+y2)/2)
        center_target=x,y        
        print(center_target)
        if abs(angle_i-angle_j)<10:
            cv.circle(frame,center_target,4,(0,255,0),5)
    except:
        print('nahi mila')
    cv.imshow('a',frame)
    if cv.waitKey(10)==27:
        break
cv.destroyAllWindows()
cap.release()