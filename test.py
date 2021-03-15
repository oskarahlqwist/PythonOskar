import random
"""
file = open('D:\Kodning\Python projekt\Fortsattning kodning\inlamningsuppgift_hangagubbe\ordlista.txt').readlines() # file.txt är bara namnet på fieln  r är för reda 
line = file[0]
words = line.split() 
myword = random.choice(words)
print(myword)"""


import random
print(random.choice(open('D:\Kodning\Python projekt\Fortsattning kodning\inlamningsuppgift_hangagubbe\ordlista.txt').read().split()))