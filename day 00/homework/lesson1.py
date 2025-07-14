from turtle import *

speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square 

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows
color("blue")
penup()
goto(80,200)
pendown()

penup()

forward(70)
left(210)

pendown()

forward(35)
left(90)

forward(35)
right(90)
right(180)
forward(35)
left(90)
forward(35)

color("blue")
penup()
goto(83,174)
forward(72)
pendown()

forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)

exitonclick()