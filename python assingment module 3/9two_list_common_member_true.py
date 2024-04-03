'''Oue9 :- Write a Python function that takes two lists and returns true if they have
          at least one common member.'''

# Ans:- 

list1 =[1,2,3,4,5,6]
list2 = [12,11,7,8,9,5,6]

for i in list1:
    for j in list2:     
        if i==j:
            print("True")

