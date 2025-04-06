# Lesson 12 - While Loops

# Recap 1: Multiples of 3 and 5
# Create a program to check if a number is both divisible by 3
# and 5.

# 1. Ask the user to input a number
# 2. Using the '%' operator, check if the number is both a
#    multiple of 3 and 5:
#     If true, print "The number is divisible by 3 and 5!"
# 3. Else, print "The number is not divisible by 3 and 5"

# ans=int(input("number?"))
# if ans%3==0 and ans%5==0:
#     print("divisible")
# else:
#     print("not divisible")

# Task 1: Introduction to while loop
# **Task 1a**:
# Due to a pandemic, the government placed a limit to the number
# of visitors a venue can have.

# Using a 'while' loop, create a program that will increase the
# number of visitors by 1 before printing out the number of
# visitors admitted, until number of visitors reaches 50.

# 1. Create a 'visitors' variable and assign '0' to it
# 2. While there is less than 50 visitors,
#     I. Increase the visitor count by 1
#     II. Print the visitor count

# (For Task 1b & 1c)
# Modify your program to account for the number of visitors
# already present at the venue, and the number of maximum visitors
# allowed for the following:

# **Task 1b**:
# Visitors already present: 18
# Max visitors allowed: 30
visitors=18
while visitors < 30:
    visitors=visitors+1
    print(visitors)

# **Task 1c**:
# Visitors already present: 4
# Max visitors allowed: 25
visitors=4
while visitors < 25:
    visitors=visitors+1
    print(visitors)


# visitors=0
# while visitors < 50:
#     visitors=visitors+1
#     print(visitors)

# Task 2: while... break
# A restaurant used to have a max capacity of 50. However, due to
# the worsening of the pandemic, the government has restricted the
# max capacity of the restaurant to 30.

# Using an 'if' condition and 'break' within the 'while' loop,
# modify your answer for Task 1a to terminate the 'while' loop when
# number of visitors is 30.
# visitors=0
# while visitors < 50:
#     visitors=visitors+1
#     print(visitors)
#     if visitors==30:
#         break

# Task 3: Order taking using while loop
# Using what you have learnt so far, code a program to take a
# customer's order.

# Declare a variable called 'order' and assign an empty string
# variable "" to it.

# Using a 'while' loop:
# 1. Ask the user to enter their order
# 2. For each order entered, concatenate to the 'order' variable.
# 3. Exit the 'while' loop if the user enters "end"
# 4. On program end, print out the customer's order.

# **Bonus**
# 1. Modify your code to remove the comma (",") that appears
#    either at the start or end of your sentence
while order != "end":
    order=input("foood????")
    order=order+","+order
print

