s = 'HOW now Brown cow??'
caps,small = 0,0
for char in s:
    if char.isalpha():
         if char.islower():
             small += 1
         else:
             caps += 1
print('Det finns')
print(caps,'versaler')
print(small,'gemena i:')
print(s)
