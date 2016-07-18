import numpy as np
import cv2
from matplotlib import  pyplot as plt
import scipy.misc

# img = cv2.imread('IMGWA0010.jpeg')
img = cv2.imread('IMGWA0019.jpeg')
# img = cv2.imread('IMGWA0024.jpeg')
w,h = img.shape[:2]
print(w)
print(h)
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (50,50,450,290)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
# plt.axis("off")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# # plt.imshow(img)
# plt.show()
###############
scipy.misc.imsave('outBitumin.jpeg', img)
#cv2.imwrite(img,'myGray.jpeg')
plt.imshow(img),plt.colorbar(),plt.show()
