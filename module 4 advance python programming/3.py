# Que3:- Write a Python program to append text to a file and display the text.

# Ans:-

text = "# Hello World"
f = open("ques.txt",'a')

f.write(text)
f.write("\n")
f.close()
