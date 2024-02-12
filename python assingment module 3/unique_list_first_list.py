# Que11 :- Write a Python function that takes a list and returns a new list with unique
#        elements of the first list

# Ans :-

list = [1,2,3,4,5,2,3,1]
unique_list =[]

for s in list:
    if s not in unique_list:
        unique_list.append(s)
print(unique_list)
