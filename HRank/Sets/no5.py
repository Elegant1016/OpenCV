_ = input()

set1 = {int(i)for i in input().split()}

l = []
N = int(input())
for i in range(N):
    cmdArray = input().split()
    if cmdArray[0] == "remove":
        set1.remove(int(cmdArray[1]))
    elif cmdArray[0] == "discard":
        set1.discard(int(cmdArray[1]))
    elif cmdArray[0] == "pop":
        set1.pop()

print(sum(set1))