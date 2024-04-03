'''
Que6 :- Write a Python program to count the number of strings where the string
       length is 2 or more and the first and last character are same from a given
       list of strings.'''

list = ["pavan","nitin","anuska","naina","jaya","harsh"]
count = 0
for s in list:
    count += 1                  
    if s[0] == s[-1]:       # close
        print(s)
print(count,"elements in list")

    
    
    

