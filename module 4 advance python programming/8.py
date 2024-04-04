# Que8:- Write a python program to find the longest words.

# Ans:-

list1 = ["anushka", "krishna", "nitin", "jai"]

longestWord = list1[0]

for word in list1:
    if len(word) > len(longestWord):
        longestWord = word


print(f"Longest word in given list is {longestWord}")
