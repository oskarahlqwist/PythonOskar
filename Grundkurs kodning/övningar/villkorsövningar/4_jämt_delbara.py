tal1 = int(input('Ange täljare: '))
tal2 = int(input('Ange nämnare: '))

if tal2 == 0:
    print('ett tal kan inte divideras med 0')

elif tal1 % tal2 == 0:
    print(tal1,'och', tal2,'kan divideras jämt')

else:
    print(tal1,'och', tal2,'kan inte divideras jämt')