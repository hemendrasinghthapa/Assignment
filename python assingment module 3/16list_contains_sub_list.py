# Que16:- Write a Python program to check whether a list contains a sub list

# Ans :- close 

main_list = [1, 2, 3, 4, 5, 6, 7]
sublist = [3, 4, 5]

found = False
for i in range(len(main_list) - len(sublist) + 1):
    if main_list[i:i + len(sublist)] == sublist:
        found = True
        break

if found:
    print("The sublist", sublist, "is present in the main list", main_list)
else:
    print("The sublist", sublist, "is not present in the main list", main_list)
