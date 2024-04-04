# Que6:-Write a Python program to read a file line by line and store it into a list

# Ans:-

file_path = 'ques.txt'
lines = []

with open(file_path, 'r') as file:
    for line in file:
        lines.append(line.strip())  # Strip to remove leading/trailing whitespaces and newline characters



print("the file stored in a list:")
for i in lines:
    print(i)



