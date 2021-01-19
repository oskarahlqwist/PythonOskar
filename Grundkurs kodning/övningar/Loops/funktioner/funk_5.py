'''ABC = ['abcdefghijklmnopqrstuvwxyz']

def mult(tal1):
    for i in range(1, lim+1):
        print(tal1, "X", i, "=", tal1 * i)
    for x in range(len(ABC)):

tal1 = int(input("Skriv talet: "))
lim = int(input("Upp till vilket tal ska talet multipliceras med?: "))

result = mult(tal1)
'''

def multiptabell(tal):
    for i in range(11):
        print(str(i) + "*" + str(tal) + " = " + str(i*tal))


tal = int(input("Skriv in ett tal: "))
multiptabell(tal)