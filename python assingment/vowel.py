a = input("enter letter :").lower()
if a.isalpha():
    if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
        print("vowel")
    else:
        print("not vowel")
else:
    print("invalid input")