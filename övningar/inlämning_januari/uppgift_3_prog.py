#"Sorority World" består av ett antal tjejer som läser vid ett fiktivt amerikanskt universitet och bor på en så-kallad "sorority". 
#Världen representeras av en mängd tjejer modellerat som en lista (members) och två predikat (likes(x,y), rooms_with(x,y) ).
#De sistnämnda modelleras som dictionaries.

#Ditt program skall möta följande krav:
#1.) Lista alla medlemmar i föreningen.
#2.) Tala om vem som personen X gillar.
#3.) Tala om vem som personen X delar rum med.
#4.) Avlsuta

#Tilläggskrav:

#Om X inte finns, skriv ut att denne inte är med i föreningen.

#Fråga 2: om X gillar alla (förutom se själv) skriv:
#"X gillar alla"

#Fråga 2: om X inte gillar någon skriv:
#"X tycker inte om någon"

from create_sorority_world import pickle
with open("sorority_world.p", "rb") as f:
    members,likes,rooms_with = pickle.load(f) 

askname = input("Skriv namn: ")

if askname in members:
    print(askname,"gillar: ", likes[askname])
    print("och delar rum med:", rooms_with[askname])
else:
    print(askname, "är inte med i föreningen")

#Gör en funktion som kollar om askname gillar alla. Om alla namn förutom sitt eget finns i members gillar hon alla.

friends = ['Augusta','Charmain','Billie','Mandy','Charlotte','Lesley']

if askname in friends:
    friends.remove(askname)

if friends in (likes[askname]):
    print (askname, "gillar alla")

#Gör en funktion som kollar om askname gillar ingen. Om inga namn dyker upp members gillar hon ingen.



#print (members)
#print (likes)
#print (rooms_with)
