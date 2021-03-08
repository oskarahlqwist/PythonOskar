import random


HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

WORDS = [
    'CASA', 'CARRO', 'MONO', 'ESTERNOCLEIDOMASTOIDEO', 'PYTHON', 'DJANGO',
    'MILTON', 'LENIS', 'SWAPPS', 'LOGIA', 'UNITTESTING'
]

class Hangagubbe():
    """
    
    """

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

    def is_invalid_letter(self, input_):
          
        """
        Method to validate if an user input is not just a letter (it means the
        input is a number or a text with more than 1 char)
        :param input_: String, user input to be validated
        """
        return (len(input_) > 1)

    def print_game_status(self):
        """
        Method to print the word to guess blankspaces with the remaining
        attempts and the guessed letters
        """
        # We append withespaces both sides to make the game look prettier
        print('\n')
        print('\n'.join(HANGMAN[:self.fails]))
        print('\n')
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
            user_input = input('\nSkriv en bokstav: ')
            if user_input.isalpha():
                user_input = user_input.upper()
                return user_input
            
            else:
                return(user_input,'är inte en bokstav')
           

    def play(self):
        """
        Method to play the game, it prompts the user for a letter and plays
        the game until the user guesses the word or lose his attempts
        """
        while self.fails < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()

            # Validate the user input
            if self.is_invalid_letter(user_input):
                print(user_input,'är inte EN bokstav')
                continue
            # Check if the letter is not already guessed
            if user_input in self.game_play:
                print('Du har redan gissat den bokstaven')
                continue

            if user_input in self.the_word:
                indexes = self.indexes(user_input)
                self.update_progress(user_input, indexes)
                # If there is no letter to find in the word
                if self.game_play.count('_') == 0:
                    print('\n¡Yay! You win!')
                    print('The word is: {0}'.format(self.the_word))
                    quit()
            else:
                self.fails += 1
        print("\n¡OMG! You lost!")

#if __name__ == '__main__':
the_word = random.choice(WORDS)
Hangagubbe = Hangagubbe(the_word)
Hangagubbe.play()