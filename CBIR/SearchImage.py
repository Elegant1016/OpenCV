#How to execute
#python SearchImage.py -p params.txt

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
import argparse
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import jaccard_similarity_score


class SearchImage:
    def __init__(self, paramFile):
        self.paramTxt = paramFile
        self.queryDict = dict()
        self.setQueryDict()
        self.getTrainedData()
        self.results_all = dict()
        self.materialCode = dict()
        self.trueList = []
        self.predList = []
        self.targetNames = []

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

    def setMaterialCode(self):
        # self.materialCode ={"sand":0, "bitumin":1, "gravel":2}
        self.materialCode["sand"] = 0
        self.materialCode["bitumin"] = 1
        self.materialCode["gravel"] = 2


    def processQueryImage(self):
        paramList = list()
        with open(self.paramTxt) as f:
            for line in f:
                paramList.append(int(line.strip()))
        print(paramList)
        for queryImage in self.queryDict.iterkeys():
            img = cv2.imread(queryImage)
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # radius = 3
            # noPoints = 8 * radius
            radius = paramList[0]
            noPoints = paramList[1] * radius
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

            #data = [('abc', 121),('qwe', 231),('pop', 148), ('gfh',221)]
            #sorted(data, key=lambda x:x[1])
            #sorted(data, key=lambda x:x[1], reverse=True)
            results = sorted(results, key=lambda score: score[1])

            self.results_all[queryImage] = results
            print("Displaying scores for {} ** \n".format(queryImage))
            for k in self.materialCode.keys():
                if k in queryImage:
                    # print(k, end=" ")
                    self.trueList.append(self.materialCode.get(k))
            for k in self.materialCode.keys():
                if k in results[0][0]:
                    # print(k, end=" ")
                    self.predList.append(self.materialCode.get(k))
            for image, score in results:
                print("{} has score {}".format(image, score))
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # cv2.putText(img, 'Bitumin', (10, 450), font, 1, (255, 255, 255), 2)
            # cv2.putText(img, 'Gravel', (10, 450), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            #################################################### Code added to show in matplot lib
            # plt.axis("off")
            # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            # # plt.imshow(img)
            # plt.show()
            ######################################################
            cv2.imshow("query", img)
            ################
            # print(results)
            # print("SASAASAS" + results[0][0])
            # test = cv2.imread(results[0][0])
            # if not test is None:
            #     w, h = test.shape[:2]
            #     print(w)
            #     print(h)
            #     cv2.imshow(str(results[0][1]), cv2.imread(results[0][0]))
            #     cv2.waitKey()
            #     cv2.destroyAllWindows()
            # else:
            #     print("Not read")
            ################

            tmpImg = cv2.imread(results[0][0])
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(tmpImg, 'Bitumin', (10, 450), font, 1, (255, 255, 255), 2)

            # plt.axis("off")
            # plt.imshow(cv2.cvtColor(tmpImg, cv2.COLOR_BGR2RGB))
            # plt.imshow(tmpImg)
            # plt.show()

            cv2.imshow(str(results[0][1]), tmpImg)
            cv2.waitKey()
            cv2.destroyAllWindows()

if __name__ =="__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--params", required=True, help="Path to store all the configurable variables")
    args = vars(ap.parse_args())
    params = args["params"]

    search = SearchImage(params)
    search.setMaterialCode()
    search.processQueryImage()
    print(search.materialCode)
    tmpList = sorted(search.materialCode.items(), key=lambda x: x[1])
    for i in tmpList:
        search.targetNames.append(i[0])
    print("Actual Values :" )
    print(search.trueList)
    print("\nPredicted Values :")
    print(search.predList)
    print("\nConfusion Matrix")
    print(confusion_matrix(search.trueList, search.predList))
    print("\nClassification Report")
    print(classification_report(search.trueList, search.predList, target_names=search.targetNames))
    print("\nAccuracy Score")
    print(accuracy_score(search.trueList, search.predList))
    print("\nJaccard Similarity Score")
    print(jaccard_similarity_score(search.trueList, search.predList))

