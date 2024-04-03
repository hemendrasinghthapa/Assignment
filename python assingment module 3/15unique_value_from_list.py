# Que15:-Write a Python program to get unique values from a list

# Ans:-
list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for i in list:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)


