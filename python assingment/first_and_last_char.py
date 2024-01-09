a = input("enter a string : ")

if len(a)>1:

    new_str = a[:2]+a[-2:]
    print(new_str)
else: 
    print(a)
