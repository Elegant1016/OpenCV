import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy
#complete argument-processing library
import argparse

parserObj = argparse.ArgumentParser(description="This is the test")
parserObj.add_argument("-i", "--image", help="Provide image path")
parserObj.add_argument("-H", "--host", help="Provode host ip")
parserObj.add_argument("-p", "--port", help="Provode Port")
nameSpace = parserObj.parse_args()
a = vars(nameSpace)
print(a)
