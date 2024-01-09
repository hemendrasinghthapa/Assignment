
a = input("enter a string1 :")
b = input("enter a string2 : ")

new_str = b[:2]+ a[2:] +" "+ a[:2]+ b[2:]

print(new_str)