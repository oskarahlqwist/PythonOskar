import random
# ger nya bool-värden för om det finns hinder framför
def look_ahead():
    low = random.choice([True, False])
    high = random.choice([True, False])
    return low, high

energi = 10
# fortsätt tills batteriet tar slut
while True:
    energi -= 1
    low_obstacle, high_obstacle = look_ahead()

    if energi <= 0:
        break
    elif low_obstacle == True and high_obstacle == True:
        print("snurrhoppa")
    elif low_obstacle == True:
        print("rulla")
    else:
        print("hoppa")