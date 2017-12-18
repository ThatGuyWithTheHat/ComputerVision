# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 17:38:47 2017

@author: mattd
"""




def saveImg(frame):
    cv2.imwrite('TestPicture.png', frame)
    

cam = cv2.VideoCapture(0)
time.sleep(2)

while True:
    ret,frame = cam.read()
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        saveImg(frame)
        break

cam.release()
cv2.destroyAllWindows()

