import cv2
import numpy as np
from matplotlib import pyplot as plt
import scipy.misc

#open and read the image
img = cv2.imread("outfile.jpeg")

w,h = img.shape[:2]
print(w)
print(h)


mask = np.zeros(img.shape[:2], dtype = "uint8")
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)
cv2.rectangle(mask, (cX - 100, cY - 100), (cX + 65 , cY + 65), 255,-1)
# cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

gray = cv2.cvtColor(masked,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,1,255,cv2.THRESH_BINARY)

_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)

crop = img[y:y+h,x:x+w]
cv2.imwrite('sofwinres.jpeg',crop)

