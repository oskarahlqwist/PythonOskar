import random
import turtle 
from tkinter import *
t = turtle.Turtle()
t.speed('fastest')
#Bestämmer storlek på 
t.pensize(5)

#Målar upp ställningen till spelet
t.penup()
t.goto(-50,0)
t.pendown()

t.color('brown')
t.forward(100)
t.right(180)
t.forward(50)
t.right(90)
t.forward(170)
t.rt(90)
t.fd(100)
t.right(90)
t.forward(25)
t.penup()
t.right(90)
t.pendown()

t.color('yellow')
t.speed(5)

#Struktur för turtle
HANGMAN = ['1','2','3','4','5','6']

ORDET = []
ordlista = ['KINGEN']
gissade_bokstäver=[]
#tar fram slumpmässigt ord ur ordlistan och öppnar ordlista
ORDET.append(random.choice(ordlista))
# file = open('ordlista1.txt','r') # file.txt är bara namnet på fieln  r är för reda 
# f = file.readlines()

# for line in f:
#     line = line.upper()
#     if line [-1]== '\n':  # ifall att sista index ordet i listan är \n 
#         ordlista.append(line[:-1])
#     else:
#         ordlista.append(line)  



class Hangagubbe():
  
    def __init__(self, the_word):
        self.fails = 0
        self.the_word = the_word
        self.game_play = list('_' * len(self.the_word))
        self.gissade_bokstäver=[]
        
    def indexes(self, letter):
        """ Räknar hur många bostäver det slumpmässiga ordet har """
        return [i for i, char in enumerate(self.the_word) if letter == char]
        # gåringenom "the_word" retunerar index för varje bokstav i ordet
        # enurmarete gör varje bokstav i "the_word" med till hörande index till ett "object" "tupel"

    def check_input(self, input_): 
        """ Kontrollerar att gissningen är EN bokstav """
        return (input_.isdigit() or len(input_) > 1) 

    def print_game_status(self):
        """Lägger till mellanrum mellan _ i terminalen samt kallar på game_play"""
        print(' '.join(self.game_play))
    
    def check_gissade_bokstäver(self, letter):
        """Kontrollerar att bokstaven inte redan gissats på och printar vilka bokstäver som gissat"""
        if letter not in self.gissade_bokstäver:
            self.gissade_bokstäver.append(letter)
            print("\n""Använda bokstäver: ", " ".join(self.gissade_bokstäver))        

    def update_progress(self, letter, indexes):
        """ Kollar va"""
        for index in indexes:
            self.game_play[index] = letter

    def get_user_input(self):
      #tar in user input och kontrollerar att det är en bokstav samt hanterar ifall det är versal/icke-versal
            user_input = input('\nGissa en bokstav: ')
            if user_input.isalpha():
                user_input = user_input.upper()
                return user_input
            else:
                return(user_input)
 
    def play(self):
        #startar spelet genom att fråga om en första bokstav och fortsätter tills spelaren inte har några försök kvar
    
        while self.fails < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()
            #Lägger till bokstaven i en lista
            self.check_gissade_bokstäver(user_input)
            
            # Kontrollerar ifall bokstaven redan gissats
            if user_input in self.game_play:
                print('Du har redan gissat på den bokstaven')
                continue

            if user_input in self.the_word:
                indexes = self.indexes(user_input)
                self.update_progress(user_input, indexes)

                if self.game_play.count('_') == 0:
                    print('\n DU VANN!')
                    t.speed('slow')
                    t.color('black')
                    style = ('Arial', 30, 'italic')
                    t.penup()
                    t.goto(0,-50)
                    t.pendown()
                    t.write('DU VANN :D ', font=style, align='center')
                    turtle.done()
                    print('Ordet är: {0}'.format(self.the_word))
                    quit()
            else:
                self.fails += 1
                if self.fails==1:
                    
                    t.circle(20)
                    t.left(90)
                    t.penup()
                    t.forward(40)
                    print("Du har 5 försök kvar")
                elif self.fails==2:
                    print("Du har 4 försök kvar")
                    t.pendown()
                    t.forward(20)
                elif self.fails==3:
                    print("Du har 3 försök kvar")
                    t.right(120)
                    t.forward(40)
                    t.right(180)
                    t.forward(40)
                elif self.fails==4:
                    print("Du har 2 försök kvar")
                    t.left(60)
                    t.forward(40)
                    t.left(180)
                    t.forward(40)
                    t.left(60)
                    t.forward(30)
                elif self.fails==5:
                    print("Du har 1 försök kvar")
                    t.left(30)
                    t.forward(45)
                    t.right(180)
                    t.forward(45)
                elif self.fails==6:
                    t.left(120)
                    t.forward(45)
                
        print("\n DU FÖRLORA")
        t.speed('slow')
        t.color('black')
        style = ('Arial', 30, 'italic')
        t.penup()
        t.goto(0,-50)
        t.pendown()
        t.write('LOOSER!', font=style, align='center')
        turtle.done()
        print('Ordet var: {0}'.format(self.the_word))
        quit()
        


the_word = random.choice(ORDET)
Hangagubbe = Hangagubbe(the_word)
Hangagubbe.play()