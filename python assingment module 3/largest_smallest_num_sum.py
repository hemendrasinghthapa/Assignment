'''Que4 : - Write a Python function to get the largest number, smallest num and sum
        of all from a list.
'''

# Ans:-

list = [1,2,3,4,5]
longest = list[0]           # Longest  number for a finding code in a list  
for i in list:            
    if i>longest:
        longest=i
print("longest num : ",longest)
sum = 0
for num in list:
    sum = num+sum
print("sum : - ",sum)

# Ans:-

list1 = [9,2,3,4,6,7,8]
smallest = list1[0]             # Smallest number for a finding code in a list                 
for s in list1:
    if s<smallest:
        smallest=s
print("smallest num : ",smallest)
sum = 0
for num in list1:
    sum = num+sum
print("sum :- ",sum)