N = int(input().strip())
# l = [ int(i) for i in input().strip().split(" ")]
l = [ int(i) for i in input().split()]
unique = set(l)
l = list(unique)
l.sort(reverse=True)
print (l[1])

# return sorted(set(l))[-2]
# n=input()
# a=map(int,input().split())
# a=list(set(a))
# a.remove(max(a))
# print (max(a))


#
# def findSM(l):
#     f, s = l[0], l[0]
#     for i in range(len(l)):
#         if l[i] > f:
#             s, f = f, l[i]
#         elif l[i] < f:
#             if f == s:
#                 s = l[i]
#             elif l[i] > s:
#                 s = l[i]
#     return s
#
# n = int(input())
# l = input().split()
# for i in range(n):
#     l[i] = int(l[i])
#
# print(findSM(l))

# max1 = -102
# max2 = -101
# for i in arr:
#     if max1<i:
#         max2 = max1
#         max1 = i
#     elif max1!=i and max2<i:
#         max2 = i
# print (max2)