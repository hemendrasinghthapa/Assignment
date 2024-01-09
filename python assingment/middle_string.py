str = input("enter a string : ")

length = len (str)
length = length//2
str1 = input("enter a string : ")
new_str = str[:length]+" "+str1+" "+str[length:]
print(new_str) 