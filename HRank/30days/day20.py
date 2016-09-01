import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

i = 0
count = 0
while i < len(a):
    swap = 0
    j=0
    while j < len(a) - 1:
        if(a[j] > a[j+1]):
            tmp = a[j]
            a[j] = a[j+1]
            a[j + 1] = tmp
            swap += 1
            count += 1
        j += 1
    i += 1
    if swap == 0:
        break

print("Array is sorted in %d swaps." %(count))
print("First Element: %d" %(a[0]))
print("Last Element: %d" %(a[len(a)-1]))

'''
def merge_sort(A):
    if len(A) <= 1:
        return 0, A
    middle = len(A)/2
    left_inversions, left = merge_sort(A[:middle])
    right_inversions, right = merge_sort(A[middle:])
    merge_inversions, merged = merge(left, right)
    inversions = left_inversions + right_inversions + merge_inversions
    return inversions, merged
def merge(left, right):
    result = []
    i, j, inversions = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            inversions += j
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    inversions += j*(len(left)-i)
    result += left[i:]
    result += right[j:]
    return inversions, result


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
count, sa = merge_sort(a)


print 'Array is sorted in %s swaps.\nFirst Element: %s\nLast Element: %s'%(count,sa[0],sa[n-1])
'''

