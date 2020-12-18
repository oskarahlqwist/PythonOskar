
s = 'doo bee doo bee doo doo doo'
substr = 'doo'
lista = []
offset = 0
result = s.find(substr)
while result != -1:
    lista.append(result+offset)
    offset += result+len(substr)
    s = s[result+len(substr):]
    result = s.find(substr)
print(lista)
