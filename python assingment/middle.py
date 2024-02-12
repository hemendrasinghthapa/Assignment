str1 = input("enter a string1 : ")

length = len(str1)
length = length//2
str2 = input("enter a string2 : ")
new = str1[:length]+" "+ str2+" "+str1[length:]
print(new)