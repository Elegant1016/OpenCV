N = int(input())
for i in range(N):
    temp = input()
    even= temp[::2]
    odd = temp[1::2]
    print(even + "  " + odd)

