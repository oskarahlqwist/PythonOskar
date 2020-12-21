import pickle
members = ['Augusta','Charmain','Billie','Mandy','Charlotte','Lesley']
likes = {'Augusta':['Charmain','Billie','Mandy','Charlotte','Lesley'],'Charmain':['Augusta','Mandy'],'Billie':['Augusta','Charmain','Lesley',],'Mandy':['Charlotte','Billie','Augusta'],'Lesley':['Billie']}
rooms_with = {'Augusta':'Charmain','Charmain':'Augusta','Billie':'Lesley','Lesley': 'Billie','Charlotte':'Mandy','Mandy':'Charlotte'}

with open("sorority_world.p", "wb") as f:
    pickle.dump((members,likes,rooms_with), f)

