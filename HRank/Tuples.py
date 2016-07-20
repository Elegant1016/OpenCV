N = int(input().strip())
l = []
for i in range(N):
    l = (input().split(" "))
    if(len(l) >= N):
        l = l[:N]
        break

print(tuple(l))
print(hash(tuple(l)))

# input()
# print (hash(tuple(map(int, input().strip().split(" ")))))

n=int(input())
T=tuple([int(i) for i in input().split()])
print(hash(T))