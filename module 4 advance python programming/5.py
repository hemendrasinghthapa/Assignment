# Que5:-Write a Python program to read last n lines of a file.

# Ans:-

f = open("ques.txt",'r')

text = f.read()
print(text[::-1])

f.close()
