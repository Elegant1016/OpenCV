data = [('abc', 121),('qwe', 231),('pop', 14), ('gfh',221), ('zaw', 150),('qwe', 100)]


#sorting using the explicit function for key
def getKey(item):
    return item[1]
print(sorted(data, key=getKey))


#Sorting using the Lambda function
print(sorted(data, key=lambda key:key[1], reverse=True))

import argparse
import os

parseArgs = argparse.ArgumentParser()
parseArgs.add_argument("-i", "--image", help="Please provide image file")

args = vars(parseArgs.parse_args())

SEPARATOR = ";"

# if os.listdir("/home/santosh/SamplePics") == []:

label = 0
for dirname, dirnames, filenames in os.walk("/home/santosh/SamplePics"):
    for subdirname in dirnames:
        subject_path = os.path.join(dirname, subdirname)
        print(subject_path)
        for filename in os.listdir(subject_path):
            abs_path = "%s/%s" % (subject_path, filename)
            print("%s%s%d" % (abs_path, SEPARATOR, label))
        label = label + 1

