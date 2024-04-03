# Que51:- Write a Python function that checks whether a passed string is
# palindrome or not. 

# Ans:-

name =  input("enter a name : ")
if name[::-1]==name[0::]:
    print("palindrome")
else:
    print("palindrome not")

