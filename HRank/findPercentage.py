# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# n = int(input())
# mydict = dict()
# for line in range(n):
#     info = input().split(" ")
#     score = map(float, info[1:])
#     mydict[info[0]] = list(score)
#
# score = mydict.get(input())
# print("%.2f" %(sum(score) / len(score)))

data = {}
for _ in range(int(input())):
    name, *marks = input().split()
    data[name] = [float(m) for m in marks]
marks = data[input()]
print("%.2f" % (sum(marks)/len(marks)))


