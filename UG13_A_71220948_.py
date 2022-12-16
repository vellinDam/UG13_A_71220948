import turtle
t = turtle.Turtle()

turtle.Screen().bgcolor("black")
t.pensize(5)
t.pencolor("pink")

#huruf V
t.left(300)
t.forward(100)
t.left(120)
t.forward(100)
t.left(90)
t.forward(10)
t.left(90)
t.forward(85)
t.left(240)
t.forward(85)
t.left(90)
t.forward(10)

#angka 9
t.penup()
t.goto(60.0)
t.pendown()
t.right(-45)
t.left(180)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

#huruf D
t.up()
t.goto(0,-210)
t.down()
t.left(90)
t.forward(175)
t.left(90)
t.circle(90,180)

