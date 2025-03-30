# print("Hello from lesson 9")
# name=input("What is your name? ")
# print("Nice to meet you, "+name+"!")


start=int(input("Whats the starting number?"))
end=int(input("Whats the ending number?"))
increament=int(input("Whats the increament number?"))
for i in range(start,end+1,increament):
    print(i)