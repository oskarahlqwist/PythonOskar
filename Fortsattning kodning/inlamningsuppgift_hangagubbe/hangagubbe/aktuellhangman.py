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


#Hur många försök man får
antal_liv = ['1','2','3','4','5','6']

class Hangagubbe():
    def __init__(self, ordet):
        self.gissningar = 0
        self.ordet = ordet
        self.ord_status = list('_' * len(self.ordet))
        self.gissade_bokstaver = []

    def indexes(self, bokstav):
        """Går in genom varje bokstav i ordet retunerar en lista med index och bokstav"""
        return [i for i, char in enumerate(self.ordet) if bokstav == char]
    
    def check_bokstav(self, bokstav): 
        """Kollar också om bokstaven är en siffra, längre än 2 tecken eller redan gissats på."""
        if bokstav in self.gissade_bokstaver:
            print('\nDu har redan gissat på den bokstaven')

        if len(bokstav) > 1:
            print('\nDu skrev fler än ett tecken')

        if bokstav.isdigit():
            print('\nSiffror är inte tillåtna')

    def print_ord_status(self):
        """
        Lägger till mellanrum mellan _ i terminalen samt kallar på ord_status
        printar bokstäver som du gissat rätt och sätter " _ " på där bokstäver saknas
        """
        print(' '.join(self.ord_status))
    
    def check_gissade_bokstaver(self, bokstav):
        """Lägger till bokstaven i en lista med använda bokstäver och printar ut.
        Kontrollerar att bokstaven inte redan gissats på och printar vilka bokstäver som gissats."""
        if bokstav not in self.gissade_bokstaver:
            self.gissade_bokstaver.append(bokstav)
        if bokstav.isdigit() or int(len(bokstav)) > 1:
            self.gissade_bokstaver.remove(bokstav)
        print("\n""Använda bokstäver: ", " ".join(self.gissade_bokstaver))

    def update_ord_status(self, bokstav, index):
        """Tar in indexet i ordet som bokstaven ligger i och lägger in den bokstaven på rätt index i ord_status."""
        for i in index:
            self.ord_status[i] = bokstav

    def get_gissad_bokstav(self):
        """Tar in user input och kontrollerar att det är en bokstav samt hanterar ifall det är versal/icke-versal"""
        gissad_bokstav = input('\nGissa en bokstav: ')
        if gissad_bokstav.isalpha():
            gissad_bokstav = gissad_bokstav.upper()
            return gissad_bokstav
        else:
            return(gissad_bokstav)
        
    def spela(self):
        #Startar spelet genom att fråga om en första bokstav och fortsätter tills ord_status inte har några försök kvar
        while self.gissningar < len(antal_liv):
            self.print_ord_status()
            gissad_bokstav = self.get_gissad_bokstav()
            
            # Kontrollerar felinmatniing
            self.check_bokstav(gissad_bokstav)

            #Lägger till bokstaven i en lista med gissade bokstäver
            self.check_gissade_bokstaver(gissad_bokstav)

            ##Tar ut vilken plats/index i ordet bokstaven ligger på.
            if gissad_bokstav in self.ordet:
                indexes = self.indexes(gissad_bokstav)
                self.update_ord_status(gissad_bokstav, indexes)
                
                if self.ord_status.count('_') == 0:
                    print('\nDU VANN!')
                    t.speed('slow')
                    t.color('black')
                    style = ('Arial', 30, 'italic')
                    t.penup()
                    t.goto(0,-50)
                    t.pendown()
                    t.write('DU VANN :D ', font=style, align='center')
                    print('Ordet var: {0}'.format(self.ordet))
                    turtle.done()
                    
            else:
                self.gissningar += 1
                if self.gissningar==1:
                    t.circle(20)
                    t.left(90)
                    t.penup()
                    t.forward(40)
                    print("Du har 5 försök kvar\n")
                elif self.gissningar==2:
                    print("Du har 4 försök kvar\n")
                    t.pendown()
                    t.forward(20)
                elif self.gissningar==3:
                    print("Du har 3 försök kvar\n")
                    t.right(120)
                    t.forward(40)
                    t.right(180)
                    t.forward(40)
                elif self.gissningar==4:
                    print("Du har 2 försök kvar\n")
                    t.left(60)
                    t.forward(40)
                    t.left(180)
                    t.forward(40)
                    t.left(60)
                    t.forward(30)
                elif self.gissningar==5:
                    print("Du har 1 försök kvar\n")
                    t.left(30)
                    t.forward(45)
                    t.right(180)
                    t.forward(45)
                elif self.gissningar==6:
                    t.left(120)
                    t.forward(45)

        print("\nDU FÖRLORA")
        t.speed('slow')
        t.color('black')
        style = ('Arial', 30, 'italic')
        t.penup()
        t.goto(0,-50)
        t.pendown()
        t.write('LOOSER!', font=style, align='center')
        print('Ordet var: {0}'.format(self.ordet))
        turtle.done()

try:
    ordlista = 'ordlista.txt'
    ordet = random.choice(open(ordlista).read().split())
    ordet = ordet.upper()
    Hangagubbe = Hangagubbe(ordet)
    Hangagubbe.spela()
except FileNotFoundError:
    print("\nordlista.txt hittades inte.\nProva istället att kopiera in pathen i","ordlista = 'ordlista.txt'")