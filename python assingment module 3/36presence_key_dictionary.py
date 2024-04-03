# Que36:-How Do You Check The Presence Of A Key In A Dictionary?

# Ans:-

dic1={
    1:23,
    2:45,
    3:34,
    4:32,
}

k = int(input("enter presence key: "))
if k in dic1.keys():
    print("yes,presence ky")
else:
    print("not presence key")
