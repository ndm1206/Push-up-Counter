import time
import cv2
import cvzone
import numpy as np
from cvzone.PoseModule import PoseDetector
 
# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot access camera")
    exit()

# Initialize pose detector
detector = PoseDetector()
ptime = 0
ctime = 0
color = (0, 0, 255)
direction = 0
push_ups = 0
while True:
    _, img = cap.read()
    img = detector.findPose(img)
    lmlst,bbox=detector.findPosition(img,draw=False)
    if lmlst:
        # Calculate angles for both arms
        a1 = detector.findAngle(img, 12, 14, 16)
        a2 = detector.findAngle(img, 15, 13, 11)
        
        # Map angles to percentage and bar values
        per_val1 = int(np.interp(a1, (85, 175), (100, 0)))
        per_val2 = int(np.interp(a2, (85, 175), (100, 0)))
        bar_val1 = int(np.interp(per_val1, (0, 100), (40 + 350, 40)))
        bar_val2 = int(np.interp(per_val2, (0, 100), (40 + 350, 40)))
        
        # Draw bars for left arm
        cv2.rectangle(img, (570, bar_val2), (570 + 35, 40 + 350), color, cv2.FILLED)
        cv2.rectangle(img, (570, 40), (570 + 35, 40 + 350), (), 3)
        
        # Draw bars for right arm
        cv2.rectangle(img, (35, bar_val1), (35 + 35, 40 + 350), color, cv2.FILLED)
        cv2.rectangle(img, (35, 40), (35 + 35, 40 + 350), (), 3)
        
        # Display percentage values
        cvzone.putTextRect(img, f'{per_val2}%', (35, 25), 1.1, 2, colorT=(255, 255, 255), colorR=color, border=3)
        cvzone.putTextRect(img, f'{per_val1}%', (570, 25), 1.1, 2, colorT=(255, 255, 255), colorR=color, border=3)
        
        # Push-up counter logic
        if per_val1 == 100 and per_val2 == 100:
            if direction == 0:
                push_ups += 0.5
                direction = 1
                color = (0, 255, 0)
        elif per_val1 == 0 and per_val2 == 0:
            if direction == 1:
                push_ups += 0.5
                direction = 0
                color = (0, 255, 0)
        else:
            color = (0, 0, 255)
        
        cvzone.putTextRect(img, f'Push_Ups: {int(push_ups)}', (209, 35), 2, 2, colorT=(255, 255, 255), colorR=(255, 0, 0), border=3)
        cvzone.putTextRect(img, 'Left Hand', (15, 350 + 80), 1.4, 2, colorT=(255, 255, 255), colorR=(255, 0, 0), border=3)
        cvzone.putTextRect(img, 'Right Hand', (495, 350 + 80), 1.4, 2, colorT=(255, 255, 255), colorR=(255, 0, 0), border=3)
        
        # Calculate and display FPS
        ctime = time.time()
        if ptime > 0:
            fps = 1 / (ctime - ptime)
            cvzone.putTextRect(img, f'FPS: {int(fps)}', (288, 440), 1.6, 2, colorT=(255, 255, 255), colorR=(0, 135, 0), border=2)
        ptime = ctime



    cv2.imshow('Push-Ups Counter', img)
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
