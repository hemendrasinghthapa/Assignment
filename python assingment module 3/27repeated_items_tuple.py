# Que27:-Write a Python program to find the repeated items of a tuple.

# Ans:-

tuple=(1,2,3,4,5,2,1)
new_tuple=[]
r=[]
for i in tuple:
    if i not in new_tuple:
       new_tuple.append(i)
    else:
       r.append(i)
print(r)
