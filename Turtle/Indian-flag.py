import turtle
t=turtle.Turtle()
t.speed(10)

t.up()
t.goto(-100,-300)
t.down()
t.setheading(90)
t.forward(500)
t.setheading(0)
for i in range(2):
    t.forward(400)
    t.right(90)
    t.forward(100)
    t.right(90)
    
    


turtle.done()