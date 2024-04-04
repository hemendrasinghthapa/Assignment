# Que7:-Write a Python program to read a file line by line store it into a variable.

# Ans:-

file_path = 'ques.txt'
lines = []

with open(file_path, 'r') as file:
    for line in file:
        lines.append(line.strip())  # Strip to remove leading/trailing whitespaces and newline characters

str = ""  #variable where whole text will we stored

print("Contents of the file stored into a varianble:")
for i in lines:
    str = str + i + "\n"

print(str)

