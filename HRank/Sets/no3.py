#No Idea!
_,_ = input().split()
arr = [int (i ) for i in input().split()]
setArr = set(arr)


set1 = set([int(i)for i in input().split()])
set2 = set([int(i)for i in input().split()])

happ = 0
for i in arr:
    if i in set1: happ+=1
    elif i in set2: happ-=1
print(happ)

# _, L = input(), tuple(map(int, input().split()))
# A, B = {int(x) for x in input().split()}, {int(y) for y in input().split()}
# XD   = 0
#
# for i in L:
#     if   i in A: XD += 1
#     elif i in B: XD -= 1
# print(XD)





