
### pip install opencv-contrib-python
import cv2
from object_detector import *
import numpy as np
from skimage.morphology import remove_small_objects
from skimage.measure import label

# Load Aruco detector
parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)


# Load Object Detector
detector = HomogeneousBgDetector()

# Load Image
img = cv2.imread("input3.jpg")

# Get Aruco marker
corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)

# Draw polygon around the marker
int_corners = np.int0(corners)
cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

# Aruco Perimeter
aruco_perimeter = cv2.arcLength(corners[0], True)

# Pixel to cm ratio
pixel_cm_ratio = aruco_perimeter / 20
contours = detector.detect_objects(img)
fasulye = []
nohut = []
# Draw objects boundaries
for cnt in contours:
    # Get rect
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

    # Get Width and Height of the Objects by applying the Ratio pixel to cm
    
    object_width = w / pixel_cm_ratio
    object_height = h / pixel_cm_ratio
    
 
    # Display rectangle
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    if object_height<3 and object_width<3:
        
        if object_width>(1.5*object_height)  or object_height>(1.5*object_width):
            fasulye.append(object_width)
            cv2.putText(img, 'fasulye', (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
            cv2.polylines(img, [box], True, (0, 0, 255), 2)
            
            
        else:
            nohut.append(object_width)
            cv2.putText(img, "nohut", (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            cv2.polylines(img, [box], True, (255, 0, 0), 2)
            
    else:
        break

a = len(fasulye)
b = len(nohut)
print(len(fasulye))
print(len(nohut))
cv2.putText(img, f"Fasulye sayisi {a} , Nohut sayisi {b}", (int(x - 100), int(y + 500)), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

  
cv2.imshow("Image", img)
cv2.waitKey(0)