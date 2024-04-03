# Que50:- Write a Python function to check whether a number is perfect or not.

# Ans:-

sum=0
num=int(input("enter a number "))
for i in range(1,num):
    if num%i==0:
        sum=sum+i
print(sum)

if num==sum:
    print("perfect number")
else:
    print("not perfect number")

