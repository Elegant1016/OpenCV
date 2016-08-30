#How to run this file
#python CreateCSV.py -t trainset -i train.txt
#python CreateCSV.py -t queryset -i query.txt


import os.path
import sys
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--trainset", required=True, help="Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required=True, help="Path to where the computed index will be stored")
args = vars(ap.parse_args())

# open the output index file for writing
output = open(args["index"], "w")

SEPARATOR = ";"

label = 0
for dirname, dirnames, filenames in os.walk(args["trainset"]):
    for subdirname in dirnames:
        subject_path = os.path.join(dirname, subdirname)
        for filename in os.listdir(subject_path):
            abs_path = "%s/%s" % (subject_path, filename)
            output.write("%s%s%s\n" % (abs_path, SEPARATOR, label))
            print("%s%s%d" % (abs_path, SEPARATOR, label))
        label = label + 1

# close the index file
output.close()


