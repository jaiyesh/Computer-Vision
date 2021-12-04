import cv2
#in opencv x axis is towards right and y axis is towards below> So origin of image is at top left corner

#Resize Image: We need to know current size of image

img = cv2.imread('Resources/lambo.png')
print(img.shape) #462,623,3 =height,width and rbh channels
imgResize = cv2.resize(img,(300,200)) #width,height
stretchimg = cv2.resize(img,(1000,500))
cv2.imshow('Og Image',img)
cv2.imshow('Resize Image',imgResize)
cv2.imshow('Strecthed Image',stretchimg)
print(f'Resized image is {imgResize.shape}')

cv2.waitKey(0)

#Cropping Image: Images are matrics of numbers

imgCropped = img[200:400,200:500] #Cropping heught and Width
cv2.imshow('Cropped Image', imgCropped)
cv2.imshow('OG Image', img)
cv2.waitKey(0)