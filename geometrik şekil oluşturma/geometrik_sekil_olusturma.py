# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 02:45:12 2022

@author: figen
"""

####GEOMETRİK ŞEKİL ÇİZME
import numpy as np
import cv2

img = cv2.imread('kare.jpg', 1)
cv2.imshow('image', img)
img = np.zeros([600, 800, 3], np.uint8)

img = cv2.line(img, (0,0), (255,255), (147, 96, 44), 10) # 44, 96, 147
img = cv2.arrowedLine(img, (0,355), (255,255), (255, 0, 0), 10)


font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)

img = cv2.ellipse(img,(640,500),(100,60),0,0,333,255,-1)  
img = cv2.ellipse(img,(640,300),(100,60),0,0,275,255,-1)  
img = cv2.ellipse(img,(640,100),(100,60),0,0,360,255,1)  

img = cv2.rectangle(img, (284, 500), (510, 300), (0, 0, 255), 10)
img = cv2.circle(img, (400, 400), 63, (0, 255, 0), -1)

pts = np.array([[284,300],[390,100],[510,300]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,0,255))   #ÜÇGEN ÇİZME
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows() 