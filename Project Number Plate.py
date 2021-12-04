import cv2




#####################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_russian_plate_number.xml')  # Pretarained model
minArea = 500
color = (255,0,255)
################################
cap = cv2.VideoCapture(0)
#Video is sequence of images, so while loop for going throiufgh each frame one by one
cap.set(3,640)# 3 is width and 640 pixels
cap.set(4,480)#4 is height and 480 pixels
cap.set(10,100) #10 for brigthness
count = 0

while True:
    success, img = cap.read()  #It will save image in img and tell whether success or not(True or False)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberplates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)  # Finding faces

    # Rectangles around face
    for (x, y, w, h) in numberplates:  # x,y,widht,height of faces
        area = w*h
        if area>minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,'Number Plate',(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
        imgRoi = img[y:y+h,x:x+w]
        cv2.imshow('ROI',imgRoi)


    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xFF ==ord('s'):  #Deklay and q for breaking the loop
        #Saving images
        cv2.imwrite('Resources/saved/NoPlate_'+str(count)+'.jpg',imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,'Scan Saved',(150,265),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(0,0,255),2)
        cv2.imshow('Result',img)
        cv2.waitKey(500)
        count+=1