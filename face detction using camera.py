import cv2
import numpy as np
# Pretrained Model will be used here
faceCascade = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_frontalface_default.xml') # Pretarained model
cap = cv2.VideoCapture(0)
#Video is sequence of images, so while loop for going throiufgh each frame one by one
cap.set(3,640)# 3 is width and 640 pixels
cap.set(4,480)#4 is height and 480 pixels
cap.set(10,100) #10 for brigthness







while True:
    success, img = cap.read()  #It will save image in img and tell whether success or not(True or False)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)  # Finding faces

    # Rectangles around face
    for (x, y, w, h) in faces:  # x,y,widht,height
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):  #Deklay and q for breaking the loop
        break