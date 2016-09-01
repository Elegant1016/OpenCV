N = int(input().strip())
l = list()
for i in range(N):
    l.append([input(), float(input())])

second_lowest = sorted(list(set([marks for name, marks in l])))[1]
print('\n'.join([a for a,b in sorted(l) if b == second_lowest]))

# inp = [[raw_input(),float(raw_input())] for i in range(input())]
#
# fl=list(set([i[1] for i in inp]))
# fl.sort()
# p=fl[1]
# inp=filter(lambda x:x[1]==p,inp)
# inp.sort()
# for i in inp:
#     print i[0]