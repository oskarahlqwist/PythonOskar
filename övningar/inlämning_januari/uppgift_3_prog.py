#"Sorority World" består av ett antal tjejer som läser vid ett fiktivt amerikanskt universitet och bor på en så-kallad "sorority". 
#Världen representeras av en mängd tjejer modellerat som en lista (members) och två predikat (likes(x,y), rooms_with(x,y) ).
#De sistnämnda modelleras som dictionaries.

#Ditt program skall möta följande krav:
#1.) Lista alla medlemmar i föreningen.
#2.) Tala om vem som personen X gillar.
#3.) Tala om vem som personen X delar rum med.
#4.) Avsluta

#Tilläggskrav:

#Om X inte finns, skriv ut att denne inte är med i föreningen.

#Fråga 2: om X gillar alla (förutom se själv) skriv:
#"X gillar alla"

#Fråga 2: om X inte gillar någon skriv:
#"X tycker inte om någon"

from create_sorority_world import pickle
with open("sorority_world.p", "rb") as f:
    members,likes,rooms_with = pickle.load(f) 

def checkMembers():
    print (members)

def checkRoomates(askName):
    askName = input("Skriv namn: ")
    if askName in members:
        print("och delar rum med:", rooms_with[askName])
    else:
        print(askName, "är inte med i föreningen")

def checkLikes():
    askName = input("Skriv namn: ")
    likeAll = ['Augusta','Charmain','Billie','Mandy','Charlotte','Lesley']
    askFriends = likes.get(askName)
    likeAll.sort() 
    askFriends.sort() 
    
    if askName in members:
        print(askName,"gillar: ", likes[askName])
    
    if askName in likeAll:
        likeAll.remove(askName)
    
    if likeAll == askFriends: 
        print (askName, "gillar alla")

meny == True
while meny:
    print("1.Lista alla medlemmar i föreningen.")
    print("2.Tala om vem som personen X gillar".
    print("3.Tala om vem som personen X delar rum med.")
    print("4. Avsluta.")
    alternativ = input("kör: ")
    if alternativ == "1":
        checkMembers()
    elif alternativ == "2":
        checkLikes()
    elif alternativ == "3":
        checkRoomates()
    else:
        meny == False