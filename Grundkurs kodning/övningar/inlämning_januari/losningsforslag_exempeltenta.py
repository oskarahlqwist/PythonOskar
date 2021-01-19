###UPPGIFT 5, Kodförståelse###

def a1(l):              #Denna funktion a1() tar ett argument
    i = len(l)-1        #tilldelar variabeln i värdet av (antalet element i aktuell lista)-1.
    while i >= 0:       #Så länge som i är större än eller lika med 0
        print(l[i])     #skriv ut listindex motsvarande värdet av i. Eftersom listindex börjar räkna upp från 0 används "-1" för att i ska matcha detta hela vägen genom listan.
        i = i - 1       #Värdet av i kommer för varje varv att minska med 1. 
                        #(Alltså backar utskriften ett steg i listan för varje gång loopen körs. 
                        # Villkoret gör också att att loopen slutar när variabeln i nått listindex 0.)

        
def a2(l):              #Denna funktion a2() tar ett argument
    i = 0               #och variabeln i tilldelas värdet 0, som motsvarar första elementet i listindexeringen
    while i < len(l):   #Så länge som värdet av i är mindre än värdet av antalet element i listan
        print(l[i])     #skriv ut listindex som motsvarar värdet av i
        i +=2           #för varje varv ökar i med 2, vilket gör att utskriften hoppar två steg fram i listan för varje varv som ovan villkor gäller.
        
lista = [5, 10, 34, 56, 96, 100]    #Listan består av en serie heltal
a1(lista)                           #kör funktion a1 av listan (lista), (börja i slutet och hoppa hela tiden ett steg tillbaka)
a2(lista)                           #kör funktion a1 av listan (lista)  (börja från början och skriv ut varannat element i listan)


input()
####UPPGIFT 6, LISTOR#######
lista = ["John","Jenny", "Agneta", "Lisa", "Adam", "Brian", "Gary", "Nils","Tina", "Zena","Örjan"]

letter_a_to_m = ["A","B","C","D","E","F","G","H","I","J","K","L","M"]
letter_n_to_ö = ["N","O","P","Q","R","S","T","U","V","X","Y","Z","Å","Ä","Ö"]

names_a_to_m = []
names_n_to_ö = []
for i in lista:
    if(i[0]) in letter_a_to_m:
        names_a_to_m.append(i)
    elif(i[0]) in letter_n_to_ö:
        names_n_to_ö.append(i)

names_a_to_m.sort()
names_n_to_ö.sort()

print("A-M", names_a_to_m, "\nN-Ö", names_n_to_ö)

input()
####UPPGIFT 7, INMATNING OCH TYPOMVANDLING#####

#a) Skriv kod som läser in två olika sifferinputs (en i taget) från användaren och sedan använder dessa för att
#skriva ut:
# 1. Resultatet man får när man adderar tal 1 och tal2
# 2. Resultatet man får när man subtraherar tal 1 och tal2
# 3. Resultatet man får när man dividerar tal 1 med tal2
# 4. Resultatet man får när man multiplicerar tal 1 med tal2

tal1=int(input("Tal 1: "))
tal2=int(input("Tal 2: "))

print(str(tal1+tal2)+"\n"+str(tal1-tal2)+"\n"+str(tal1/tal2)+\
    "\n"+str(tal1*tal2))

input()
#b) Två möjliga felkällor är här om användaren skriver in input som inte består av siffror, samt om användaren
#skriver in input som leder till division med noll i punkt 3 (detta är ju matematiskt omöjligt, och kommer
#därför att krascha programmet). Lägg till kod som förhindrar detta. O
tal1=input("Tal 1: ")
tal2=input("Tal 2: ")

calculate=False
while calculate==False:
    if tal1.isdigit() and tal2.isdigit():
        if int(tal2)==0:
            while int(tal2)==0:
                print("Fel! Tal två får inte vara 0!")
                tal2=(input("Tal 2: "))
        print(str(int(tal1)+int(tal2))+"\n"+str(int(tal1)-int(tal2))+\
    "\n"+str(int(tal1)/int(tal2))+"\n"+str(int(tal1)*int(tal2))+"\n")
        calculate=True
    else:
        print("Fel! Både tal 1 och 2 måste vara heltal!")
        tal1=input("Tal 1: ")
        tal2=input("Tal 2: ")

input()
###UPPGIFT 8, FUNKTIONER###
#a)
def calculation(tal1, tal2):
    calculate=False
    while calculate==False:
        if tal1.isdigit() and tal2.isdigit():
            if int(tal2)==0:
                while int(tal2)==0:
                    print("Fel! Tal två får inte vara 0!")
                    tal2=(input("Tal 2: "))
            addition=       int(tal1)+int(tal2)
            subtraction=    int(tal1)-int(tal2)
            division=       int(tal1)/int(tal2)
            multiplication= int(tal1)*int(tal2)
            calculate=      True
        else:
            print("Fel! Både tal 1 och 2 måste vara heltal!")
            tal1=input("Tal 1: ")
            tal2=input("Tal 2: ")
    calculations= (addition, subtraction, division, multiplication)
    return calculations

#b)
tal1=input("Tal 1: ")
tal2=input("Tal 2: ")
ariths=["+","-","/","*",]
n=-1
for i in (calculation(tal1, tal2)):
    n=n+1
    print(tal1, ariths[n], tal2,"=", end="")
    print("",i)

input()
###UPPGIFT 9)###
loopactive=True
while loopactive==True:
    import random
    throwrange=10
    throws=[]
    for i in range(throwrange):
        dice = random.randint(1,6)
        throws.append(dice)
        print(dice)
    total=sum(throws)
    print("Average is;", total/throwrange)
    exitprogram=input("Enter 'E' to exit.")
    exitcommands=("E","e")
    if exitprogram in exitcommands:
        loopactive=False

input()
###UPPGIFT 10, Villkorsatser###
print("Välkommen till 'Gissa Rätt'!\nEnter 'E' to exit.")
loopactive=True
while loopactive==True:
    import random
    throwrange=1
    throws=[]
    for i in range(throwrange):
        dice = random.randint(1,6)
        throws.append(dice)
    guess=input("Gissa vad tärningen visade:")
    if guess.isdigit():
        if int(guess)==throws[0]:
            print("Rätt!")
        elif int(guess)>throws[0]:
            print("FÖR HÖGT")
        else:
            print("FÖR LÅGT")
        exitcommands=("E","e")
    if guess in exitcommands:
        loopactive=False

    print ("Rätt svar var:", dice)
    input()

input()
###Uppgift 11, Dictionaries###

namn=input("Namn: ")
nummer=input("Telefonnummer: ")
d={"Viktor": "18153", "Johan": "16108", "Andreas":"18857", "Robin":"24039", namn:nummer}
print (d)

search=input("Skriv nummret till den du söker: ")
for i in d:
    if search in d[i]:
        print ("Numret tillhör:",i)