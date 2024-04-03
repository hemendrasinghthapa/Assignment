# Que 7:- Write a Python program to remove duplicates from a list.

# Ans:-  

list1 = [1,2,34,5,6,7,34,2]
list2= [] # empty string to store and compare with list1
for s in list1:            # for loop for compare 
    if s not in list2:   
        list2.append(s) # after compare to remove duplicate used append
print(list2)