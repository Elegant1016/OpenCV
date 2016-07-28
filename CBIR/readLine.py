from operator import itemgetter

paramList = list()
with open('params.txt') as f:
    for line in f:
        paramList.append(int(line.strip()))
print (paramList)

materialCode = dict()
materialCode["sand"] = 0
materialCode["bitumin"] = 1
materialCode["gravel"] = 2
trueList = []
predList = []

#
# str1 = "queryset/testMaterial/gravelTest4.jpeg"
# str2 = "trainset/bitumin/ref8.jpeg"
#
# for k in materialCode.keys():
#     if k in str2:
#         print(k,end=" ")
#         trueList.append(materialCode.get(k))
#         print(materialCode.get(k))
# for k in materialCode.keys():
#     if k in str1:
#         print(k,end=" ")
#         trueList.append(materialCode.get(k))
#         print(materialCode.get(k))
#
# print(trueList)


# print(sorted(materialCode.values()))
# print(sorted(materialCode.items(), key=itemgetter(1)))
# print(sorted([(value, key) for (key,value) in materialCode.items()]))

l = sorted(materialCode.items(), key=lambda x: x[1])
for i in l:
    print(i[0])

print(materialCode)