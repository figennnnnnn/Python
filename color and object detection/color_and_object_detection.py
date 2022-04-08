# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:20:05 2022

@author: figen
"""

import cv2

cap = cv2.VideoCapture(0)

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)
hlist = []
sayi = 0 
while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape
    # Extract Region of interest
    roi=frame[250:350,80:240]
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

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
                    cv2.rectangle(roi, (x,y),(x+w,y+h), (255,255,0),3)
                    sayi += 1
                    print (f"{sayi}. top geçti" )
                    
                    hcomp0 = hsv_frame[x:x+w,y:y+h, 0]
                    mean = int(hcomp0.mean())
                    hue_value = mean
    
                    color = "Undefined"
                    if hue_value <5:
                        color = "red"
                    elif hue_value < 22:
                        color = "orange"
                    elif hue_value < 33:
                        color = "YELLOW"
                    elif hue_value < 78:
                        color = "GREEN"
                    elif hue_value < 131:
                        color = "BLUE"
                    elif hue_value < 167:
                        color = "VIOLET"
                    else:
                        color = "RED"
                    
                    cv2.putText(frame, color, (x - 50, 100), 0, 3, (mean), 5)
            else:
                hlist = []
                
    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()