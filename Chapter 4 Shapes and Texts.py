import cv2
import numpy as np

img = np.zeros((512,512,3)) #Black Image rgb 3 channels

img[:] = 255,0,0 #Blue
img[:] = 0,255,0 #Green
img[:] = 0,0,255 #Red


#Line creation
cv2.line(img,(0,0),(300,300),(0,255,255),2) #Starting point,ending point,color,thickness
#Rectangle
cv2.rectangle(img,(10,10),(300,300),(255,0,255),2)
#Circle
cv2.circle(img,(400,50),30,(255,255,0),6) # center point, radius

#Put texts on images
cv2.putText(img,' Open CV is fun ',(250,250),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(255,150,34),2)

cv2.imshow('Image',img)
cv2.waitKey(0)