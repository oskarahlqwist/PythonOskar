#övning 1

def make_sum(n):
    if (n >= 1):
        print(n,'+','f (',n-1,')')
        return (n + make_sum(n - 1))
    else:
        return 0
try:
    n = int(input("Enter an integer: "))
except:
    print("You must key in an integer")
    exit(1)

total = make_sum(n)
print("Sum of integers in",n,"is",total)

#övning 2
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2)) 

num = int(input('skriv in nummret: '))

if num <= 0 :
    print('skriv in ett poitivt tal : ')
else:
    print('fibonacci sequence:')
    for i in range(num): #  för i range in num / inputen 
        print(fibonacci(i))