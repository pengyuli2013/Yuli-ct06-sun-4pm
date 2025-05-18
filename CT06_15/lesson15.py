# # Lesson 15 - Functions

# ## Recap 1: Turtle drawing
# **Recap 1a**:
# Using the 'turtle' library, create a 200x200 window

# 1. Import 'turtle' library
# 2. Using '.setup()', create a window 200 in width and 200 in height
# 3. Add a '.mainloop()' function to keep the window open

# **Recap 1b**:
# Modify your previous code to create a blue arrow as your turtle.

# 1. Create a turtle called "artist" using 'turtle.Turtle()'
# 2. Using '.shape()', change the turtle shape to "arrow"
# 3. Using '.color()', change the turtle color to "blue"

# **Recap 1c**:
# Modify your previous code to draw the shape of a compass rose (shown
# on screen)

# 1. Use '.penup()' and position turtle to (0, 0) using '.goto()'
# 2. Point turtle towards North ("90") using '.seth()'
# 3. Use '.pendown()' and draw "60" towards North
# 4. Using '.right()', turn turtle 90 degrees to the right 
# 5. Using a 'for' loop, draw a circle by moving 1 step each time
#    before turning 1 degree to the right for 360 times.

# **Recap 1d**:
# Modify your previous code to print the position of your turtle at the
# end of the drawing.

# 1. Using '.xcor()' and 'ycor()' and '.write(text)', print your turtle's
#    last coordinates in the following format:

#    "Current turtle position: <x>, <y>"

# print("Hello from lesson 14")
# import turtle
# window=turtle.Screen()
# window.setup(200,200)
# artist = turtle.Turtle()
# artist.shape("arrow")
# artist.color("blue")
# artist.seth(90)
# artist.penup()
# artist.goto(0,0)
# artist.pendown()

# artist.forward(60)
# artist.left(90)
# for i in range(360):
#     artist.forward(1)
#     artist.left(1)

# ## Task 1: Self-introduction
# You are at a party, and you expect to see your friend Ethan and 3 of
# his friends you have never met before. They are Ben, Gracie, and
# Javior.

# Write a program (with or without functions) that will ask the user
# for their name and print 1 of 3 ways to greet the person:
# 1. If the person is Ethan, greet him by saying:
#         "Hi Ethan. How are you?"
# 2. If the person is either Ben, Gracie, or Javior, greet them by
#    saying:
#         "Hi there!"
#         "My name is Freddo"
#         "I like to swim and eat chicken wings!"
#         "Nice to meet you!"
# 3. If the person is none of the above, say:
#         "I don't think you belong here..."
# def welcome():
#     print("hi")
#     print("my name is freddo")
#     print("i like to swim and eat chicken wings")
#     print("nice to meet u")

# var=input("name")
# if var=="ethan":
#     print("hi")
# elif var=="ben" or var=="gracie" or var=="javior":
#     welcome()
# else:
#     print("u dont belomng here")


# def doubleNum(Num):
#     return Num*2
# Num=input("Num?")
# print(doubleNum(Num))

import turtle
def set_up(screen_width,screen_height):
    screen=turtle.Screen()
    screen.setup(width=screen_width,height=screen_height)
    return screen
screenwidth=300
screenheight=500
screen=set_up(screenwidth,screenheight)
def create_blue_ball():
    ball=turtle.Turtle()
    ball.shape("circle")
    ball.color("blue")
    ball.penup()
    return ball
ball=create_blue_ball()
ball.goto(0,0)
def move_ball(ball, dx,dy):
    ball.setx(ball.xcor()+dx)
    ball.sety(ball.ycor()+dy)
def check_x(ball,screenwidth):
    if ball.xcor()>(screenwidth/2)or ball.xcor() < (-screenwidth/2):
        return True
def check_y(ball,screenwidth):
    if ball.ycor()>(screenWidth/2)or ball.ycor() < (-screenWidth/2):
        return True
    
dx=2
dy=2
while True:
    move_ball(ball,dx,dy)
    if check_x(ball, screenwidth):
        dx*=-1

screen.mainloop()

    


































































































































































































# def strsquare():
#     for i in range(4):
#         turtle.forward(20)
#         turtle.right(90)


# square=6
# rows=3
# for i in range (rows):
#     for i in range(square):
#         square()







































































# artist.mainloop()