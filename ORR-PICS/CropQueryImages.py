import numpy as np
import cv2
from matplotlib import  pyplot as plt
import scipy.misc
import csv
import numpy as np
import argparse


def cropQuerySet(filename):
    with open(filename, "rb") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            img = cv2.imread(row[0])
            mask = np.zeros(img.shape[:2], np.uint8)

            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            rect = (50, 50, 450, 290)
            cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
            img = img * mask2[:, :, np.newaxis]
            fname = row[0]
            fname = fname[0:fname.find('.')]
            outFile = fname + "out" + ".jpeg"
            scipy.misc.imsave(outFile, img)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True, help="Path to the file that contains the indexs")
    args = vars(ap.parse_args())
    params = args["file"]

    cropQuerySet(args["file"])
