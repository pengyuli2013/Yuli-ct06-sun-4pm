# print("Hello from lesson 8")
# num1=int(input("what is da first num"))
# num2=int(input("what is da second num"))
# num3=int(input("what is da third num"))
# num4=int(input("what is da fourth num"))
# num5=int(input("what is da fifth num"))
# num6=str(num1*num2*num3*num4*num5)
# print("the product is "+num6)
import time
num=int(input("count down from which number"))
for i in range(num,0,-1):
    print(i)
    time.sleep(1)