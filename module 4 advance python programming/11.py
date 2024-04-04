# Que11:-Write a Python program to write a list to a file.

# Ans:-

file_path = 'ques.txt'

list1 = ["anita", "jai", "pooja", "nitin"]

with open(file_path, 'a') as file:
    for i in list1:
        file.write(i + "\n")