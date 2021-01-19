lista1 = []
antal_namn = int(input("Hur många namn vill du skriva?: "))
for x in range (0,antal_namn):
    print("Skriv namn {}: ".format(x+1))
    namn = (input())
    lista1.append(namn)
print ("Alla namn på listan är: ", lista1)

kalle = namn.count("Kalle")
print("Antal Kalle på listan: ", kalle)
