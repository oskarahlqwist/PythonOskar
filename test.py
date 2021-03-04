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