import cv2

#img = cv2.imread("Resources/lena.png")  #Image reading

#cv2.imshow('Output',img) #Name of window, image to show
#cv2.waitKey(0) #Delay for showing image: 0 for infiniote delay

# for video capture:

# cap = cv2.VideoCapture("Resources/test.mp4")
# #Video is sequence of images, so while loop for going throiufgh each frame one by one
#
# while True:
#     success, img = cap.read()  #It will save image in img and tell whether success or not(True or False)
#     cv2.imshow('Video',img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):  #Deklay and q for breaking the loop
#         break



# for webcam:

cap = cv2.VideoCapture(0)
#Video is sequence of images, so while loop for going throiufgh each frame one by one
cap.set(3,640)# 3 is width and 640 pixels
cap.set(4,480)#4 is height and 480 pixels
cap.set(10,100) #10 for brigthness

while True:
    success, img = cap.read()  #It will save image in img and tell whether success or not(True or False)
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):  #Deklay and q for breaking the loop
        break