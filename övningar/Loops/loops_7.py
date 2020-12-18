start = int(input("Startal: "))
slut = int(input("Sluttal: "))

if start >= slut:
    print("Starttalet måste vara mindre än Sluttalet")
else:
    print("start")
    for i in range (start, slut+1):
        print (i)
        print("slut")