import cv2


img = cv2.imread('IMGWA0010.jpeg')
w,h = img.shape[:2]
print(w)
print(h)
font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'Hello World!',(10,500), font, 1,(255,255,255),2)
cv2.putText(img,'OpenCV',(10,450), font, 1,(255,255,255),2,cv2.LINE_AA)
# cv2.namedWindow("DisplaHere", cv2.WINDOW_AUTOSIZE)
cv2.imshow("DisplaHere",img)
cv2.waitKey()
