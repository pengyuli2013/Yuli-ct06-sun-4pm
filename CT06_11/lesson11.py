# var=10
# while True:
#     print(var)
#     var=var+10
#     if var>200:
#         break
# #task 1

# password="superpass123"
# ans=input("password?")
# if ans==password:
#     print("Access Granted")
# else:
#     print("Access denied")
# #task 2


planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus" ]
print(planets[2])
planets.append("neptune")
planets[3]="muskworld"
planets.pop(6)
for i in planets:
    print(i)