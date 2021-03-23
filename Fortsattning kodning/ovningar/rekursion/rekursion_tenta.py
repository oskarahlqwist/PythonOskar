def summera(n):
    if (n >= 1):
        print(n,'+','s (',n-1,')')
        return (n + summera(n - 1));
    else:
        return 0

n = int(input('Mata in ett heltal: '))
total = summera(n)
print ('Summan av heltal i intervallet 1 ...',n,'is',total) 