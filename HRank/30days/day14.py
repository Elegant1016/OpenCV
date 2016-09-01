class Difference:
    def __init__(self, a):
        self.__elements = a


    def computeDifference(self):
        m, e = 0, self.__elements
        for i in range(len(e) - 1):
            for j in range(1, len(e)):
                m = max(m, abs(e[j] - e[i]))
        self.maximumDifference = m

        # self.maximumDifference = m
        # least = min(self.__elements)
        # large = max(self.__elements)
        # self.maximumDifference = large - least

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)