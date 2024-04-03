# Que26:- Write a Python program to replace last value of tuples in a list.

# Ans:-

tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 10
for i in range(len(tuple_list)):
    tuple_list[i] = tuple_list[i][:-1] + (new_value,)

print("list of tuples:", tuple_list)





