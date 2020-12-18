age = int(input("Hur gammal är du? "))
sex = input("Vilket kön är du (kille/tjej)? ")

if age >= 18 and sex == 'kille':
    print ('Du är en kille som är myndig.')
else:
    print('Du är en kille som inte är myndig.')

if age >= 18 and sex == 'tjej':
    print ('Du är en tjej som är myndig.')
else:
    print('Du är en tjej som inte är myndig.')
