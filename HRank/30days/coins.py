def calGCD(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

num = [int(i) for i in input().split(',')]
gcd = 0
small = 0
big = 0
if min(num)<0:
    print("%d,%d"(0,0))
    exit()

else:
    if(num[0] > num[1]):
        gcd = calGCD(num[0], num[1])
    else:
        gcd  = calGCD(num[1], num[0])

count = 1
if (num[0] > num[1]):
    n = num[1]
    while(n < num[0]):
        n = n*count
        count +=1
