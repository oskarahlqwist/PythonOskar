import random
import turtle 
t = turtle.Turtle()
turtle.speed('fastest')
HANGMAN = ['1','2','3','4','5','6']

ORDET = []
ordlista = ['KINGEN']
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

    def indexes(self, letter):
        """
        tar in en bokstav och retunerar en lista med indexet på "the_word"
        """
        return [i for i, char in enumerate(self.the_word) if letter == char]
        # gåringenom "the_word" retunerar index för varje bokstav i ordet
        # enurmarete gör varje bokstav i "the_word" med till hörande index till ett "object" "tupel"

    def check_input(self, input_): # validerar input 
        """
        Method to validate if an user input is not just a letter (it means the
        input is a number or a text with more than 1 char)
        :param input_: String, user input to be validated
        """
        return (input_.isdigit() or len(input_) > 1) # kollar om bokstaven är en siffra eller längre än 2 täcken 

    def print_game_status(self):
        """
        Method to print the word to guess blankspaces with the remaining
        attempts and the guessed letters
        """
        # We append withespaces both sides to make the game look prettier
        #print('\n')
        #print('\n'.join(HANGMAN[:self.fails]))
        #print('\n')
        print(' '.join(self.game_play))

    def update_progress(self, letter, indexes):
        """
        Method to update the game progress with the guessed letters
        :param letter: String, Letter to be added to the game progress
        :param indexes: List, found occurrences (as indexes) of the given
                        letter in the word
        """
        for index in indexes:
            self.game_play[index] = letter

    def get_user_input(self):
            user_input = input('\nGissa en bokstav: ')
            if user_input.isalpha():
                user_input = user_input.upper()
                return user_input
            
            else:
                return(user_input)
           
        
    def play(self):
        """
        Method to play the game, it prompts the user for a letter and plays
        the game until the user guesses the word or lose his attempts
        """
        while self.fails < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()

            # Validate the user input
            if self.check_input(user_input):
                print(user_input,'är inte En bokstav')
                continue
            # Check if the letter is not already guessed
            if user_input in self.game_play:
                print('Du har redan gissat på den bokstaven')
                continue

            if user_input in self.the_word:
                indexes = self.indexes(user_input)
                self.update_progress(user_input, indexes)
                # If there is no letter to find in the word
                if self.game_play.count('_') == 0:
                    print('\n DU VANN!')
                    print('The word is: {0}'.format(self.the_word))
                    quit()
            else:
                self.fails += 1
                if self.fails==1:
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
        print('Ordet var: {0}'.format(self.the_word))
        quit()


#if __name__ == '__main__':
the_word = random.choice(ORDET)
Hangagubbe = Hangagubbe(the_word)
Hangagubbe.play()