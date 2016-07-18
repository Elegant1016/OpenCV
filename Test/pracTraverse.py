import os
import os.path
import sys


def visit(arg, dirnames, names):
    print("%s , %s" %(dirnames, names))
    for name in names:
        subDir = os.path.join(dirnames, name)
        if os.path.isdir(subDir):
            print("%s/" % name)
        else:
            print("%s" % name)

    print()


if not os.path.exists("example"):
    os.makedirs("example")
if not os.path.exists("example/one"):
    os.makedirs("example/one")

with open("example/one/file.txt", "wt") as f:
    f.write("Contents")

with open("example/Secfile.txt", "wt") as f:
    f.write("Contents")


for dirname, dirnames, filenames in os.walk("/home/santosh/SamplePics"):
    print ("%s , %s, %s" %(dirname, dirnames, filenames))
os.path.walk("/home/santosh/SamplePics", visit, None)
