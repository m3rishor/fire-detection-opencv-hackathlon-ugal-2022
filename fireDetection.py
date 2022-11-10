
import cv2
from playsound import playsound
import math

fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
cam = cv2.VideoCapture(0)

while(True):
    ret, Fire = cam.read()
    gray = cv2.cvtColor(Fire, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(Fire, 1.25, 5)
    
    firelen = 'Fire counter: ' + str(len(fire))

    cv2.putText(Fire,firelen,(20,35),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),3)

    for (x,y,w,h) in fire:
        aria = math.sqrt(math.pow((x+w+20)-(x-20),2)+math.pow((y+h+20)-(y-20),2))
        if (aria > 150):
            cv2.putText(Fire,'FOC MARE',(40,70),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
            playsound('audio.mp3', block=False)
        else: 
            cv2.putText(Fire,'FOC MIC',(40,70),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
            playsound('audio2.mp3', block=False)



    for (x,y,w,h) in fire:
        
        cv2.rectangle(Fire,(x-20,y-20),(x+w+20,y+h+20),(0,0,255),2)
        cv2.putText(Fire,'Fire',(x,y-30),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),3)
        for i in range(1):
            cv2.imwrite('opencv'+str(i)+'.png', Fire)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = Fire[y:y+h, x:x+w]
        print(aria)
    
        
    cv2.imshow('Fire', Fire)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
