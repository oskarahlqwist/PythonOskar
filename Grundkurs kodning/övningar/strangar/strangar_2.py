s = "HOW now Brown cow??"

upper = 0
lower = 0

for i in range (len(s)):
    if(s[i]>="a" and s[i]<="z"):
        lower += 1
    elif(s[i]>="A" and s[i]<="Z"):
        upper += 1

print(upper)
print(lower)