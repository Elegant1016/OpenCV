inpStr = input()
change = input().split()
place = int(change[0])
out = inpStr[:place] + change[1] + inpStr[place+1:]
print(out)

#Method 2
# S=raw_input()
# i,c=map(str,raw_input().split())
# i=int(i)
# print S[:i] + c + S[i+1:]