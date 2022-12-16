import turtle

s = turtle.Screen()
t = turtle.Turtle()

#huruf N
t.pensize(10)
t.pencolor('blue')
t.goto(0,150)
t.goto(100,0)
t.goto(100,150)
t.penup()

#Angka9
t.goto(200,75)
t.pendown()
t.circle(40,80)
t.circle(40)
t.goto(200,0)
t.penup()

#angka2
t.goto(300,150)
t.pendown()
t.goto(350,150)
t.goto(350,75)
t.goto(300,75)
t.goto(300,0)
t.goto(350,0)
t.penup()

#angka8
t.goto(400,50)
t.pendown()
t.circle(40,80)
t.circle(40)
t.penup()
t.goto(425,75)
t.pendown()
t.circle(40,80)
t.circle(40)
t.penup()

#hurufA
t.goto(500,0)
t.pendown()
t.goto(550,150)
t.goto(600,0)
t.penup()
t.goto(525,75)
t.pendown()
t.goto(575,75)

s.exitonclick
