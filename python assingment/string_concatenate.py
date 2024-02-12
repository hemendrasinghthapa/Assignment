str = input("enter a string : ")

if len(str) >= 3:
    if str[-3:] == "ing":
        print(str+"ly")
    else:
        str=str+"ing"
        print(str)


str = input("enter a string : ")

if len(str) >= 3:
    if str[-3:] == "ing":
        print(str+"ly")
    else:
        str = str+"ing"
        print(str)
