# Que9:-Write a Python program to count the number of lines in a text file.

# Ans:

file_path = 'ques.txt'
lines = []

with open(file_path, 'r') as file:
    for line in file:
        lines.append(line.strip())  

count = 0

for i in lines:
    count+=1

print(f"There are {count} lines in given file")

