str = "he is not poor boy "

str = str.split()
print(str)
for s in str:
    if s =="not":
        index = str.index(s)
        print(index)
        if str[index+1] == "poor":
            str.pop(index)
            str.pop(index)
            str.insert(index,"good") 

str1 = ""
for s in str:
    str1 =str1+s+" "
print(str1)