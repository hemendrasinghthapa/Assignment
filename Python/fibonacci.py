num=int(input("enter a number"))
num1=0
num2=1
print(num1)
print(num2)

for i in range(2,num+1):
    num3=num1+num2
    print(num3)
    num1=num2
    num2=num3