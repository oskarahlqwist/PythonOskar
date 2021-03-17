import random
import turtle 

t = turtle.Turtle()
t.speed('fastest')

#Bestämmer storlek på pennan
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

the_word = random.choice(open('ordlista.txt').read().split())

#Struktur för turtle
HANGMAN = ['1','2','3','4','5','6']

class Hangagubbe():
  
    def __init__(self, the_word):
        self.gissningar = 0
        self.the_word = the_word
        self.game_play = list('_' * len(self.the_word))
        self.gissade_bokstaver = []

    def indexes(self, letter):
    ##Räknar hur många bostäver det slumpmässiga ordet har
    ##tar in en bokstav och retunerar med indexet som den har i ordet
    ##går ingenom varje bokstav i ordet retunerar index för varje bokstav
    ##enurmarete gör varje bokstav i "the_word" med till hörande index till ett "object" "tupel"
        return [i for i, char in enumerate(self.the_word) if letter == char]

    def check_input(self, input_): 
    ##Kontrollerar att gissningen är EN bokstav
    ##validerar input och kontrollerar att gissningen är EN bokstav
    ## kollar om bokstaven är en siffra eller längre än 2 tecken  
        return (input_.isdigit() or len(input_) > 1) 

    def print_game_status(self):
    ##Lägger till mellanrum mellan _ i terminalen samt kallar på game_play"""
        print(' '.join(self.game_play))
    
    def check_gissade_bokstaver(self, letter):
    ##Lägger till bokstaven i en lista med använda bokstäver och printar ut
    ##Kontrollerar att bokstaven inte redan gissats på 
    ##och printar vilka bokstäver som gissat
        if letter not in self.gissade_bokstaver:
            self.gissade_bokstaver.append(letter)
            print("\n""Använda bokstäver: ", " ".join(self.gissade_bokstaver))

    def update_progress(self, letter, indexes):
    ##Tar in indexet i ordet som bokstaven ligger i och lägger in den bokstaven på rätt index i game_play.
        for index in indexes:
            self.game_play[index] = letter

    def get_user_input(self):
    ##Tar in user input och kontrollerar att det är en bokstav samt hanterar ifall det är versal/icke-versal
            user_input = input('\nGissa en bokstav: ')
            if user_input.isalpha():
                user_input = user_input.upper()
                return user_input
            else:
                return(user_input)
        
    def play(self):
        #Startar spelet genom att fråga om en första bokstav och fortsätter tills spelaren inte har några försök kvar
        while self.gissningar < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()
            #Lägger till bokstaven i en lista
            self.check_gissade_bokstaver(user_input)
            
            # Kontrollerar ifall bokstaven redan gissats
            if user_input in self.game_play:
                print('Du har redan gissat på den bokstaven')
                continue
            ##Tar ut vilken plats/index i ordet bokstaven ligger på.
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
                    print('Ordet var: {0}'.format(self.the_word))
                    quit()
            else:
                self.gissningar += 1
                if self.gissningar==1:
                    
                    t.circle(20)
                    t.left(90)
                    t.penup()
                    t.forward(40)
                    print("Du har 5 försök kvar")
                elif self.gissningar==2:
                    print("Du har 4 försök kvar")
                    t.pendown()
                    t.forward(20)
                elif self.gissningar==3:
                    print("Du har 3 försök kvar")
                    t.right(120)
                    t.forward(40)
                    t.right(180)
                    t.forward(40)
                elif self.gissningar==4:
                    print("Du har 2 försök kvar")
                    t.left(60)
                    t.forward(40)
                    t.left(180)
                    t.forward(40)
                    t.left(60)
                    t.forward(30)
                elif self.gissningar==5:
                    print("Du har 1 försök kvar")
                    t.left(30)
                    t.forward(45)
                    t.right(180)
                    t.forward(45)
                elif self.gissningar==6:
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

the_word = the_word.upper()
Hangagubbe = Hangagubbe(the_word)
Hangagubbe.play()