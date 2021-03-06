
##1
import turtle

t = turtle.Turtle()

def rektangel(x,y):
    t.forward(x)
    t.right(90)
    t.forward(y)
    t.right(90)
    t.forward(x)
    t.right(90)
    t.forward(y)

rektangel(100,200)

turtle.done()

##2
import turtle

t = turtle.Turtle()

def polygon(x,y):
    for i in range(y):
        t.forward(y)
        t.right(360/x)

polygon(5,100)


turtle.done()

##3
import turtle

t = turtle.Turtle()

t.pensize(5) 
  
t.color("blue") 
t.penup() 
t.goto(-110, -25) 
t.pendown() 
t.circle(45) 

t.color("black") 
t.penup() 
t.goto(0, -25) 
t.pendown() 
t.circle(45) 
  
t.color("red") 
t.penup() 
t.goto(110, -25) 
t.pendown() 
t.circle(45) 
  
t.color("yellow") 
t.penup() 
t.goto(-55, -75) 
t.pendown() 
t.circle(45) 
  
t.color("green") 
t.penup() 
t.goto(55, -75) 
t.pendown() 
t.circle(45) 

turtle.done()

##4

# Import required module 
import turtle 

# Create turtle object 
t = turtle.Turtle() 

# Create a screen 
screen =turtle.Screen() 

# Set background color 
screen.bgcolor("sky blue") 

# Function to draw body of snowman 
def draw_circle(color, radius, x, y): 
	t.penup() 
	t.fillcolor (color) 
	t.goto (x, y) 
	t.pendown() 
	t.begin_fill() 
	t.circle (radius) 
	t.end_fill() 

# Illustrating snowman 
# Drawing snowman body 
draw_circle ("#ffffff", 30, 0, -40) 
draw_circle ("#ffffff", 40, 0, -100) 
draw_circle ("#ffffff", 60, 0, -200) 

# Drawing left eye 
draw_circle ("#ffffff", 2, -10, -10) 

# Drawing right eye 
draw_circle ("#ffffff", 2, 10, -10) 

# Drawing nose 
draw_circle ("#FF6600", 3, 0, -15) 

# Drawing buttons on 
draw_circle ("#ffffff", 2, 0, -35) 
draw_circle ("#ffffff", 2, 0, -45) 
draw_circle ("#ffffff", 2, 0, -55) 

# Function to draw arms 
def create_line(x, y, length, angle): 
	t.penup() 
	t.goto(x, y) 
	t.setheading(angle) 
	t.pendown() 
	t.forward(length) 
	t.setheading(angle + 20) 
	t.forward(20) 
	t.penup() 
	t.back(20) 
	t.pendown() 
	t.setheading(angle - 20) 
	t.forward(20) 
	t.penup() 
	t.home() 
	
# Drawing left arm 
create_line(-70, -50, 50, 160) 

# Drawing right arm 
create_line(70, -50, 50, 20) 

# Drawing hat 
t.penup() 
t.goto (-35, 8) 
t.color ("black") 
t.pensize (6) 
t.pendown() 
t.goto (35, 8) 

t.goto (30, 8) 
t.fillcolor ("black") 
t.begin_fill() 
t.left (90) 
t.forward (15) 
t.left (90) 
t.forward (60) 
t.left (90) 
t.forward (15) 
t.end_fill()

turtle.done()

##5
import turtle

t = turtle.Turtle()
t.speed(1000)

for i in range(3):
  t.forward(200)
  t.left(120)

t.forward(95)

for i in range(36):
  t.forward(10)
  t.left(10)

t.forward(6)
t.left(90)
t.forward(172)

turtle.done()