groceries = [
    "Apples",
    "Bread",
    "Carrots",
    "Dates",
    "Eggs",
    "Flour",
    "Grapes",
    "Honey"
]
# groceries.insert(1,"bananana")
# groceries.append("ice")
# groceries[7]="herbs"
# print(groceries)
# groceries.insert(1,"bananana")
# del
for grocery in groceries:
    if grocery=="Apples":
        print("Apples: I need five of These")
    elif grocery=="Carrots":
        print("Carrots: I need three of These")
        
    

    print(grocery)

    # Task 4: Online Catalogue
# **Task 4a**:
# Write a program to create an online catalogue for a grocery store.

# 1. Using a 'while' loop, ask the user (grocery store manager) to
#    input the items their online catalogue should have.
# 3. Add each item into the catalogue list
# 4. End the loop when the user types "end"
while True:
    var=input("")

# **Task 4b**:
# Based on the list created by the grocery store manager, do the
# following:

# 1. Imagine a customer browsing the website of the grocery store.
#    Ask the customer: "What are you looking for?"
# 2. If the item is in the list, say "Yes we sell that."
# 3. Else, say "Sorry, we don't have that."
