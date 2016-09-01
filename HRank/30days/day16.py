import sys

inp = input()
try:
    print(int(inp))
except ValueError:
    # print("Oops!", sys.exc_info()[0], "occured.")
    print("Opps", sys.exc_info())
    print("Bad String")

