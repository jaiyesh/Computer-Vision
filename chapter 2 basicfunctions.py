import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')

#Convert to grayscale

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #CVT color convert ccolors into different colorspace
cv2.imshow('Gray Image', imgGray)

cv2.waitKey(0)


#Blur image

imgBlur = cv2.GaussianBlur(img,(7,7),0)  #(7,7) is blur
cv2.imshow('Blur Image', imgBlur)
#
cv2.waitKey(0)


#Edge Detector : Canny Edge Detector

imgCanny =  cv2.Canny(img,150,200)  #For reducing edges, change resolutions+ Increasing res values will find less edges

#Image Dilation = By using kernel matrices : Increasing edges thicknesses
kernel = np.ones((5,5))
imgDialation = cv2.dilate(imgCanny,kernel, iterations =1)

cv2.imshow('Dilated Image', imgDialation)

cv2.imshow("Canny EdgeDetector",imgCanny)

cv2.waitKey(0)

#Image Erosion: Making edges Thinner
imgEroded = cv2.erode(imgDialation,kernel,iterations = 1)
cv2.imshow("Canny EdgeDetector",imgCanny)
cv2.imshow('Dilated Image', imgDialation)
cv2.imshow('Eroded Image', imgEroded)
cv2.waitKey(0)
