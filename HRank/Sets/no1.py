N = int(input().strip())
arr = set([int(i)for i in input().strip().split(" ")])
print(sum(arr) / len(arr))