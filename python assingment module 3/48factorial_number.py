# Que48:- Write a Python function to calculate the factorial of a number (a
# nonnegative integer)

# Ans:-
def fact():
    f=1
    a=int(input("enter a number : "))
    for i in range(1,a+1):
        f=f*i
    print("factorial number",f)

fact()


