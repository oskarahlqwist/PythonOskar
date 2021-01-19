def storsta(tal1, tal2):
    if tal1 < tal2:
        print(tal1, "är minst")
    elif tal2 < tal1:
        print(tal2, "är minst")
    else:
        print("talen är lika stora")

tal1 = int(input("Skriv första talet: "))
tal2 = int(input("Skriv andra talet: "))
result = storsta(tal1, tal2)
