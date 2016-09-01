# N = int(input())
# set1 = set(map(int, raw_input().split()))

_ = int(input())
set1 = set([int(i)for i in input().split(" ")])

_ = int(input())
set2 = set([int(i)for i in input().split(" ")])

l = sorted((set1.difference(set2)).union(set2.difference(set1)))
# l = (set1.difference(set2)).update(set2.difference(set1))
for i in l:
    print(i)

# input()
# s1 = set(input().split())
# input()
# s2 = set(input().split())
#
# print('\n'.join(sorted((s1 - s2) | (s2 - s1), key=int)))