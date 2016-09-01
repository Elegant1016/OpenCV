# myDict= dict()
# N = int(input())
# for i in range(N):
#     arr = [item for item in input().strip().split(' ')]
#     myDict[arr[0]] = int(arr[1])
# for i in range(N):
#     key = input()
#     if myDict.get(key) != None:
#         print(key +"=" + str(myDict.get(key)))
#     else:
#         print("Not found")


n = int(input())
nameNumber = [input().split() for _ in range(n)]
phone_book = { k:int(v) for k,v in nameNumber}

# phone_book = dict(input().split() for _ in range(n))
print(len(phone_book))
for i in range(len(phone_book)):
    name = input()
    if name in phone_book:
        print('%s=%s' % (name, phone_book[name]))
    else:
        print('Not found')


# phone_book = dict(input().split() for _ in range(n))