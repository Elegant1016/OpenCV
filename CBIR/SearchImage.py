#How to execute
#python SearchImage.py

from __future__ import with_statement
import cv2
import os
from skimage.feature import local_binary_pattern
from scipy.stats import itemfreq
from sklearn.preprocessing import normalize
import cvutils
import csv
from matplotlib import pyplot as plt
import numpy as np
from sklearn.externals import joblib


class SearchImage:
    def __init__(self):
        self.queryDict = dict()
        self.setQueryDict()
        self.getTrainedData()
        self.results_all = dict()

    def setQueryDict(self):
        try:
            with open("query.txt", "rb") as csvfile:
                reader = csv.reader(csvfile, delimiter=";")

                for row in reader:
                    self.queryDict[row[0]] = int(row[1])
                print(self.queryDict)
        except:
            print("Error opening Query file")

    def getTrainedData(self):
        self.addrImg, self.lbpHistogram, self.tagNo = joblib.load("lbp.pkl")

    def processQueryImage(self):
        for queryImage in self.queryDict.iterkeys():
            img = cv2.imread(queryImage)
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            radius = 3
            noPoints = 8 * radius
            lbp = local_binary_pattern(imgGray, noPoints, radius, method='uniform')
            # Calculate the histogram
            x = itemfreq(lbp.ravel())
            # normalize the histogram
            queryHist = x[:, 1] / sum(x[:, 1])

            results = []

            for index, trainedHist in enumerate(self.lbpHistogram):
                # Distance Metric to be used, these two Low score means good
                score = cv2.compareHist(np.array(trainedHist, dtype=np.float32), np.array(queryHist, dtype=np.float32), cv2.HISTCMP_CHISQR)
                results.append((self.addrImg[index], round(score, 3)))
            results = sorted(results, key=lambda score: score[1])

            self.results_all[queryImage] = results
            print("Displaying scores for {} ** \n".format(queryImage))
            for image, score in results:
                print("{} has score {}".format(image, score))
            cv2.imshow("query", img)
            # cv2.imshow("result", cv2.imread(results[0][0]))
            cv2.imshow(str(results[0][1]), cv2.imread(results[0][0]))
            # cv2.waitKey()
            # cv2.imshow(str(results[0][1]), cv2.imread(results[1][0]))
            cv2.waitKey()
            cv2.destroyAllWindows()

if __name__ =="__main__":
    search = SearchImage()
    search.processQueryImage()

