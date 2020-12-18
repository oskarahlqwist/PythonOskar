s = 'doo     bee doo    be doo?'
blanks,tabs,others = 0,0,0
for char in s:
    if char == '\t':
         tabs += 1
    elif char == ' ':
         blanks += 1
    else:
         others += 1


print('Det finns:')
print(tabs,'tabbar')
print(blanks,'blanka')
print(others,'andra tecken i:')
print(s)
