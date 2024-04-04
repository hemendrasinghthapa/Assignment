# Que10:-Write a Python program to count the frequency of words in a file.

# Ans:-

file_path = 'ques.txt'
wordFrequency = {}

with open(file_path, 'r') as file:
    l = file.read()
    l = l.split()

for word in l:
    if word not in wordFrequency.keys():
        wordFrequency[word] = 1
    else:
        v = wordFrequency[word]
        v = v + 1
        wordFrequency[word] = v

for key, value in wordFrequency.items():
    print(f"Word : {key}, Occurence : {value}")

