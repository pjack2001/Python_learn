from PIL import Image
import cv2
import numpy as np
a=cv2.imread("a5.jpg")
kernel=np.uint8(np.zeros((5,5)))
b,g,r=cv2.split(a)
gray=cv2.cvtColor(a,6)
la=cv2.Laplacian(gray,cv2.CV_16S,ksize=3)
dst=cv2.convertScaleAbs(la)
canny=cv2.Canny(gray,1,5,1)
canny=cv2.bitwise_not(canny)

ret,thresh5=cv2.threshold(b,200,255,cv2.THRESH_BINARY)
erode=cv2.erode(gray,kernel)
erode=cv2.erode(erode,kernel)
erode=cv2.erode(erode,kernel)
cv2.imshow("a5.jpg",thresh5)
cv2.imshow("img",a)
cv2.imshow("gray",gray)
cv2.imshow("b",b)
cv2.imshow("la",dst)
cv2.imshow("canny",canny)
cv2.imshow("erode",erode)
cv2.imwrite("a6.jpg",canny)
im= Image.open("a6.jpg")
im.save("a6.jpg", dpi=(70,70))
print (im.info)
