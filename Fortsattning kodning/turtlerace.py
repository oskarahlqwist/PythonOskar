import turtle
import random

t = turtle.Turtle()
p1 = turtle.Turtle()

p1.color("blue")
p1.shape("turtle")
p1.penup()
p1.goto(-200,100)
p1.pendown()

p2 = p1.clone()
p2.color("green")
p2.shape("turtle")
p2.penup()
p2.goto(-200,-100)
p2.pendown()

t.penup()
t.goto(300,60)
t.pendown()
t.circle(40)
t.penup()
t.goto(300,-140)
t.pendown()
t.circle(40)
t.penup()

die = [50,100,150,200]

for i in range(20):
    if p1.pos() >= (300,100):
        print("Player 1 wins")
        break
    elif p2.pos() >= (300,-100):
        print("Player 2 wins")
        break
    else:
        p1_roll_dice = input("tryck enter: ")
        die_out = random.choice(die)
        print("Du slog: ", die_out)
        p1.fd(die_out)

        p2_roll_dice = input("tryck enter: ")
        die_out = random.choice(die)
        print("Du slog: ", die_out)
        p2.fd(die_out)



turtle.done()