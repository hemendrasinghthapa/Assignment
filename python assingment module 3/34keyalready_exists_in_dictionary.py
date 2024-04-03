# Que34:-Write a Python script to check if a given key already exists in a
         # dictionary.
    
# Ans:-
dic1={
    1:23,
    2:45,
    3:34,
    4:32,
}

k = int(input("enter key: "))
if k in dic1.keys():
    print("yes,given key exist")
else:
    print("not exist")



















