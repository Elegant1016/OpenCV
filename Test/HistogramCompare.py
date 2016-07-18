import cv2
import argparse
from matplotlib import pyplot as plt
from skimage.feature import local_binary_pattern
from scipy.stats import itemfreq
import numpy as np
import os

# def makeHistogram(path):
#     image = cv2.imread(path)
#     imageGray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#
#
#     radius = 3
#     noPoints = 8*radius
#     lbp = local_binary_pattern(imageGray, noPoints, radius, method='uniform')
#     x= itemfreq(lbp.ravel())
#     hist = x[:,1]/sum(x[:,1])
#     hist = np.float32(hist)
#     hist = np.float32(hist)
#     plt.plot(hist)
#     plt.show()
#
#     # hist = cv2.calcHist([imageGray], [0], None, [256], [0,256])
#     # hist = cv2.normalize(hist).flatten()
#     # hist = np.float32(hist)
#
#     # hist = cv2.equalizeHist(imageGray)
#     # hist = np.float32(hist)
#
#     # res = np.hstack((imageGray,hist)) #stacking images side-by-side
#     # cv2.imwrite('res.png', res)
#     # path = os.getcwd()
#     # path = path + "/res.png"
#     # print(path)
#     # cv2.imshow("win",cv2.imread(path))
#     # cv2.waitKey()
#     return hist
#
parseObj =argparse.ArgumentParser()
parseObj.add_argument("-i1","--image1", required="True", help="Image path needed")
parseObj.add_argument("-i2","--image2", required="True", help="Image path needed")

args = vars(parseObj.parse_args())
#
#
# hist1 = makeHistogram(args.get("image1"))
# hist2 = makeHistogram(args.get("image2"))
#
# d1 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)
# d2 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_INTERSECT)
# d3 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)
# d4 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
# print(d1)
# print(d2)
# print(d3)
# print(d4)


histArr = []
for val in args.values():
    image = cv2.imread(val)
    imagrGray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # hist = cv2.equalizeHist(imagrGray)
    # res = np.hstack((imagrGray,hist)) #stacking images side-by-side
    # cv2.imwrite('res.png', res)
    # path = os.getcwd()
    # path = path + "/res.png"
    # print(path)
    # cv2.imshow("win",cv2.imread(path))
    # cv2.waitKey()


    # histogram calculation in OpenCV
    hist = cv2.calcHist([imagrGray], [0], None, [256], [0,256])
    # hist = cv2.normalize(hist).flatten()
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()
    histArr.append(hist)
    # histogram calculation in Numpy, OpenCV histogram is much faster then numpy
    # hist,bins = np.histogram(image.ravel(),256,[0,256])
    # plt.plot(hist)
    # plt.xlim([0, 256])
    # plt.show()

print(histArr)
d1 = cv2.compareHist(histArr[0], histArr[1], cv2.HISTCMP_BHATTACHARYYA)
d2 = cv2.compareHist(histArr[0], histArr[1], cv2.HISTCMP_INTERSECT)
d3 = cv2.compareHist(histArr[0], histArr[1], cv2.HISTCMP_CHISQR)
d4 = cv2.compareHist(histArr[0], histArr[1], cv2.HISTCMP_CORREL)
print(d1)
print(d2)
print(d3)
print(d4)
