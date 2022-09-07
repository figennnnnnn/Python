# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:20:05 2022

@author: figen
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)
hlist = []
sayi = 0 
while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape
    # Extract Region of interest
    roi=frame[200:350,50:220]
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    center_coordinates = (275,135)
    radius = 60
    color= (255, 0, 0)
    thickness = -1
    image = cv2.circle(frame, center_coordinates, radius, color, thickness)
    #hsv_frame1 = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2GRAY)
    # 1. Object Detection
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        pointvalue = []
       
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
               
        if area > 500:           
            x, y, w, h = cv2.boundingRect(cnt)
            
            if y==0: 
                hlist.append(h)
                a = hlist[0]
                if h==a:
                    cv2.drawContours(frame, [cnt],-1,(255,0,0),3)
                    M=cv2.moments(cnt)
                    cx=int(M["m10"]/M["m00"])
                    cy=int(M["m01"]/M["m00"])
                    pyt=cv2.circle(frame, (cx,cy),7,(255,255,255),-1)
                    #center_coordinates = (x+(w/2), y+(h/2))
                    #image = cv2.circle(frame, center_coordinates, radius, color, thickness)
                    cv2.rectangle(roi, (x,y),(x+w,y+h), (255,255,0),3)
                    sayi += 1
                    
                    print (f"{sayi}. top geçti" )
                    
                    hcomp0 = hsv_frame[pyt, 0]
                    filter_arr = hcomp0 > 0
                    newarr = hcomp0[filter_arr]
                    mean = int(newarr.mean())
                    hue_value = mean
                    #print (sorted(newarr))
                    print (newarr)
                    print(mean)
                    color = "Undefined"
                    if (90<hue_value and hue_value<179):
                        color = "RED"
                        print(color)
                    if (22<hue_value and hue_value<38):
                        color = "YELLOW"
                        print(color)
                    if (38<hue_value and hue_value<90):
                        color = "GREEN"
                        print(color)
                    
                    cv2.putText(frame, color, (x , 100), 0, 2, mean, 5)
            else:
                hlist = []
                
    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()