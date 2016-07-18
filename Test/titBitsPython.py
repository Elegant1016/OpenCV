import numpy as np
import sys
# from scipy import stats
# from scipy.stats import itemfreq
#The difference is that flatten always returns a copy and
#ravel returns a view of the original array whenever possible.
# but if you modify the array returned by ravel, it may modify the entries in the original array.
# If you modify the entries in an array returned from flatten this will never happen. ravel will often be faster since no memory is copied,

arr = np.array(((1,2,3,4,5), (11,22,33,44,55), (111,222,333,444,555)))
print(arr.ravel())
print(arr.flatten())

# a = np.array([1, 1, 5, 0, 1, 2, 2, 67, 1, 4])
# print(stats.itemfreq(a))
# print(itemfreq(a))
# print(itemfreq(a/10.))
# print(np.bincount(a))