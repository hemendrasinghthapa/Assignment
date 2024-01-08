a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
total=a+b+c
if a==b or b==c or c==a:
    print("0")
else:
    print("total",total)