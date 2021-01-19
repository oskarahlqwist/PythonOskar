lista = []

antal = int(input('hur många tal vill du lägga till?: '))

for _ in range (0,antal):
    nytt_tal = int(input("tal: "))
    lista.append(nytt_tal)
print(lista)

'''
antal = int(input("antal heltal: "))
lista = []
i = 0
while i < antal:
    nytt_tal = int(input("tal :"))
    lista.append(nytt_tal)
    i += 1
print(i)
'''

'''
lista1 = []
antal_tal = int(input('hur många tal vill du lägga till?: '))
for x in range(0, antal_tal):
   print("Skriv tal nummer {}: ".format(x+1))
   tal = int(input())
   lista1.append(tal)
print("Listan är: ", lista1)

lista2 = []

for x in lista1:
    if x > 451: 
        lista2.append(x)
print("Alla tal i listan över 451 är: ", lista2)
'''