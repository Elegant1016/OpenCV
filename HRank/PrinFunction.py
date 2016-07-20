from sys import stdout

N = int(input().strip())

for i in range(1,N+1):
    stdout.write(str(i) + '')
for i in range(1,N+1):
    print(i,end="")

print(*range(1, int(input())+1), sep='')
for i in range(1, int(input().strip())+1):
    print (i, sep='', end='')