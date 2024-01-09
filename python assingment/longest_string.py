str = input("enter a string : ")

str = str.split()

max = str[0]

for i in str:
    word = i
    if len(word)>len(max):
        max = word
print("Longest word in given string is : ",max)