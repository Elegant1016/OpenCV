testStr = input()
testStr = [s.upper() if s.islower() else s.lower() for s in testStr]
test = ''.join(testStr)
print(test)

#To clarify: "".join(['a','b','c']) means Join all elements of the array, separated by the string "".
# In the same way, " hi ".join(["jim", "bob", "joe"]) will create "jim hi bob hi joe"

#Method2
# name = input()
# print (''.join(c.lower() if c.isupper() else c.upper() for c in name))

#Method3
# string_input = input()
# print(string_input.swapcase())