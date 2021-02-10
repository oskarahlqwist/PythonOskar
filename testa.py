class Player:
    def __init__(self, namn,position,batting_average,mlb_experience,team):
        self.__namn__ = namn
        self.__position__ = position
        self.__batting_average__ = batting_average ##float
        self.__mlb_experience__ = mlb_experience ##int        
        self.__team__ = team
        
        #get och set metoder – används inte i testfilen...    
    def __str__(self):
        return '%-20s %-8s %-8.3f %-4d %-15s' %(self.__namn__,self.__position__,self.__batting_average__, \
            self.__mlb_experience__,self.__team__)
        
        ##player_test.py
        
player_list = []
p = Player('Mike Trout','OF',.343,7,'Los Angeles Angels')
player_list.append(p)
        
p = Player('Brian Goodwin','OF',.298,9,'Los Angeles Angels')
player_list.append(p)
        
p = Player('Clayton Kershaw','P',.225,12,'Los Angeles Dodgers')
player_list.append(p)

for e in player_list:
    print(e)

elias, osakr oskar adam victor flingan valter olle