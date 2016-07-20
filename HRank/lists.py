l = []
N = int(input().strip())
for i in range(N):
    cmdArray = input().split(" ")
    # print(cmdArray)
    # if cmdArray[0] in dir(l):
    if cmdArray[0] == "insert":
        l.insert(int(cmdArray[1]), int(cmdArray[2]))
    elif cmdArray[0] == "remove":
        l.remove(int(cmdArray[1]))
    elif cmdArray[0] == "append":
        l.append(int(cmdArray[1]))
    elif cmdArray[0] == "print":
        print(l)
    elif cmdArray[0] == "sort":
        l.sort()
    elif cmdArray[0] == "reverse":
        l.reverse()
    elif cmdArray[0] == "pop":
        l.pop()

# n = input()
# l = []
# for _ in range(n):
#     s = raw_input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd)
#     else:
#         print l
