import os
import os.path
import sys

# label = 0
SEPARATOR = ";"
label = 0
def visit(arg, dirnames, names):
    # print(names)
    label = 0
    for name in names:
        subDir = os.path.join(dirnames, name)
        if os.path.isdir(subDir):
            pass
            # print("%s/" % name)
        else:
            print("%s%s%d" % (subDir, SEPARATOR, label))


    label = label + 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: create_csv <base_path>")
        sys.exit(1)

    BASE_PATH = sys.argv[1]
    os.path.walk(BASE_PATH, visit, None)



