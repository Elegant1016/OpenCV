N = int(input())
count = 0
max = 0
while N > 0:
    if N & 1 == 1:
        count = count + 1
    else:
        count = 0

    if count>max:
        max = count
    N = N>>1
print(max)

#one Liner
# print(len(max(bin(int(raw_input().strip()))[2:].split('0'))))