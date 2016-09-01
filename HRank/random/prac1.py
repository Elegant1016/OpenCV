from collections import Counter

_ = input()
ctr = Counter([int(i) for i in input().split()])

N = int(input().strip())
sum = 0
for x in range(N):
    size, cost = map(int, input().split())
    if size in ctr.keys():
        v = ctr[size]
        if v > 0:
            sum = sum + cost
        ctr[size] = v -1

print(sum)



