print("Hello from lesson 15")
import turtle

window=turtle.Screen()
window.setup(width=600,height=400)

t=turtle.Turtle()
turtle.shape("square")
t.fillcolor("orange")

## Task 3: Drawing
# Given the number of sides and each interior angle, draw each of the
# following shapes using a loop and the following functions:
#     .seth()
#     .up()
#     .down()
#     .forward()
#     .backward()
#     .left()
#     .right()

# **Task 3a**: Draw a line
# Number of sides: 1
# Interior angle: NA
# turtle.forward(10)
# # **Task 3b**: Draw a triangle
# turtle.forward(10)
# turtle.seth(60)
# turtle.forward(10)
# turtle.seth(60)
# turtle.forward(10)
# turtle.seth(60)
# # Number of sides: 3
# # Interior angle: 120

# for i in range(360):
#     t.forward(1)
#     t.left(1)

# t.penup()
# t.goto(-300,0)
# t.pendown()
# t.setx(300)

# t.penup()
# t.goto(0,200)
# t.pendown()
# t.sety(-200)

# # **Task 3c**: Draw a square
# # Number of sides: 4
# # Interior angle: 90
# turtle.forward(10)
# turtle.seth(90)
# turtle.forward(10)
# turtle.seth(90)
# turtle.forward(10)
# turtle.seth(90)
# turtle.forward(10)
# turtle.seth(90)

# **Task 3d**: Draw a pentagon
# Number of sides: 5
# Interior angle: 60
# t.forward(10)
# t.seth(60)
# t.forward(10)
# t.seth(60)
# t.forward(10)
# t.seth(60)
# t.forward(10)
# t.seth(60)
# t.forward(10)
# t.seth(60)


# # **Task 3e**: Draw a hexagon
# # Number of sides: 6
# # Interior angle: 60
# t.forward(10)
# t.seth(60)
# t.forward(10)
# t.seth(60)
# t.forward(10)
# t.seth(60)
# t.forward(10)
# t.seth(60)
# t.forward(10)
# t.seth(60)
# t.forward(10)
# t.seth(60)
# import random
# for i in range(10):
#     x=random.randint(-280,280)
#     y=random.randint(-280,280)
#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     for i in range(4):
#         t.forward(10)
#         t.seth(90)
#         t.penup()
#     t.sety(y-40)
#     t.write(t.pos(),align="centre")
xlimit=180
ylimit=180
t.penup
t.goto(xlimit,ylimit)
while True:
    t.pendown
    while t.xcor()<x_limit:
        t.forward(1)
        t.left(90)
    



# # **Task 3f**: Draw a circle
# # Number of sides: 360
# # Interior angle: 1



# for i in range(1,11):
#     print(i)
# for i in range(1,11,2):
#     print(i)





window.mainloop()
