import cv2
import numpy as np
# Pretrained Model will be used here
faceCascade = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_frontalface_default.xml') # Pretarained model



img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)  #Finding faces

#Rectangles around face
for (x,y,w,h) in faces: #x,y,widht,height of faces
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)



cv2.imshow('Image',img)
cv2.waitKey(0)