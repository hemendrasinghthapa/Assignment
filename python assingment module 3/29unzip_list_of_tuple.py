# Que29:- Write a Python program to unzip a list of tuples into individual lists.

# Ans:-


tuple = [(1 , "hemendra"),(2 , "naresh"),(3 , "kamal")]

result = list(zip(*tuple))

print(result)