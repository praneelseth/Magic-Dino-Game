import cv2
from cvzone.HandTrackingModule import HandDetector
import keyboard
import time

detector=HandDetector(detectionCon=0.8,maxHands=1)

time.sleep(2.0)

video=cv2.VideoCapture(0)

ret,frame=video.read()
hands,img=detector.findHands(frame)
cv2.imshow("Frame",frame)
time.sleep(3.0)

while True:
    ret,frame=video.read()
    hands,img=detector.findHands(frame)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
    cv2.rectangle(img, (15, 50), (295, 90), (255, 50, 255), -2)
    cv2.rectangle(img, (15, 110), (175, 150), (255, 50, 255), -2)

    if hands:
        leftHand=hands[0]
        leftFingers=detector.fingersUp(leftHand)

        count=leftFingers[0]+leftFingers[1]+leftFingers[2]+leftFingers[3]+leftFingers[4]
        if count > 0:
            cv2.putText(frame, 'Jumping!', (20,140), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            keyboard.press('up_arrow')
        else:
            keyboard.release('up_arrow')

video.release()
cv2.destroyAllWindows()