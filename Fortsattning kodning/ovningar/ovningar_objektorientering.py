#ovning1

class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

user1 = User(
    input("skriv ditt förnamn: "),
    input("skriv ditt efternamn: "),
    int(input("skriv din ålder: ")))

print(user1.first_name,", ", user1.last_name,", ", user1.age)

##DEL 2

#övning 1


##player.py

class Player:
    def __init__(self, namn,position,batting_average,mlb_experience,team):
        self.__namn__ = namn
        self.__position__ = position
        self.__batting_average__ = batting_average ##float
        self.__mlb_experience__ = mlb_experience ##int        
        self.__team__ = team
        
        #get och set metoder – används inte i testfilen...    
    def __str__(self):
        return '%-20s %-8s %-8.3f %-4d %-15s' %
        (self.__namn__,self.__position__,self.__batting_average__, \
            self.__mlb_experience__,self.__team__)
        
        ##player_test.py
        from player import Player
        
    player_list = []
    p = Player('Mike Trout','OF',.343,7,'Los Angeles Angels')
    player_list.append(p)
        
    p = Player('Brian Goodwin','OF',.298,9,'Los Angeles Angels')
    player_list.append(p)
        
    p = Player('Clayton Kershaw','P',.225,12,'Los Angeles Dodgers')
    player_list.append(p)

    for element in player_list:
        print(element)