tal = int(input("Skriv in hur många udda tal du vill skriva ut: "))

if tal < 1:
    print("Skriv bara positiva tal")

else:
    i = 1
    x = 1
    while i <= tal:
        print(x)
        x += 2
        i += 1


