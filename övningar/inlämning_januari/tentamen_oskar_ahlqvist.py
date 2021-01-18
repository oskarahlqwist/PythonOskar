#7) Inmatning och typovandling (2+2+2p)
#a)
print("Skriv första heltalet: ")
heltal1 = input()

print("Skriv andra heltalet: ")
heltal2 = input()
#b)
if heltal1.isdigit():
    print (heltal1, "är ett heltal")
else:
    print("Första talet är inte ett heltal")

if heltal2.isdigit():
    print (heltal2, "är ett heltal")
else:
    print("Andra talet är inte ett heltal")
#c)
#För att jämnt dela på ett heltal i python måste man använda modulo "%".
#Modulo fungerar så att den också skriver ut "resten" av vad som finns kvar av divisionen av ett heltal.
#Den skriver alltså också ut decimalerna som finns över.
#Till skillnad från vanliga divisionstecknet "/" som bara delar i heltal, räknar ut alla decimaler och istället avrundar neråt.

#8) Loopar (1+2+3p)
#a)
while True:
    svar = input("Skriv in q för att gå vidare")
    if svar != "q":
        print("Du skrev inte q")
        continue
    else:
        print("Du får gå vidare")
        break
#b)
x = input("Hur många stjärnor beviljas?: ")
if x.isdigit():
    print(int(x)*"*")
else:
    print("Du måste skriva ett heltal")
#c)
x = 0
while x<=10:
    print(x*"*")
    x += 1
#9) Villkorssatser (6p)
import random
# ger nya bool-värden för om det finns hinder framför
def look_ahead():
    low = random.choice([True, False])
    high = random.choice([True, False])
    return low, high

energi = 10
# fortsätt tills batteriet tar slut
while True:
    energi -= 1
    low_obstacle, high_obstacle = look_ahead()

    if energi <= 0:
        break
    elif low_obstacle == True and high_obstacle == True:
        print("snurrhoppa")
    elif low_obstacle == True:
        print("rulla")
    else:
        print("hoppa")
        
#10) Funktioner (1+2+3p)
#a)
def biggest(tal1, tal2):
    if tal1 > tal2:
        return tal1
    else:
        return tal2

tal1 = int(input("Skriv in tal 1: "))
tal2 = int(input("Skriv in tal 2: "))
    
if tal1 == tal2:
    print("tal 1 och tal 2 är lika")
else:
    print(biggest(tal1, tal2), "är det största talet.")

#b)
def addition(tal1, tal2, tal3):
    sum = tal1 + tal2 + tal3
    return sum

tal1 = int(input("Skriv in tal 1: "))
tal2 = int(input("Skriv in tal 2: "))
tal3 = int(input("Skriv in tal 3: "))

summan = addition(tal1, tal2, tal3)

print(summan)

#c)
def fullname(fornamn, efternamn):
    upperFornamn = fornamn.upper()
    upperEfternamn = efternamn.upper()
    return upperFornamn, upperEfternamn

fornamn = input("Skriv in förnamn: ")
efternamn = input("Skriv in efternamn: ")

print(fullname(fornamn, efternamn))

#11) Listor (6p)

lista = ["MacBook Pro", 126999, "iPhone SE", 4999, "iPad Pro", 11700]

priser = [i for i in lista if isinstance(i, (int, float))]
produkter = [i for i in lista if isinstance(i, (str))]

print("priser: ",priser,"\n","produkter: ", produkter)

#12) Dictionaries (4 + 2p)
#a) b)
lista = ["MacBook Pro", 126999, "iPhone SE", 4999, "iPad Pro", 11700]

priser = [i for i in lista if isinstance(i, (int, float))]
produkter = [i for i in lista if isinstance(i, (str))]

nydict = dict(zip(produkter, priser))

print(dict(nydict))

nyprodukt = input('Skriv in en produkt du vill lägga till: ')
nyttpris = int(input('Skriv in vad produkten kostar: '))
nydict.update({nyprodukt:nyttpris})
print(nydict)
