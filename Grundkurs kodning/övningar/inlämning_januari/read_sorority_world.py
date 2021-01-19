import pickle
with open("sorority_world.p", "rb") as f:
    members,likes,rooms_with = pickle.load(f) 

print (members)
print (likes)
print (rooms_with)

