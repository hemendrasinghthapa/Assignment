# Que37:-Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15.

# Ans:-

dic1 = {
    16 : 'nit',
    4 : 'anita',
    10 : 'jai',
    15 : 'mahi',
    2 : 'anuska',
    23 : 'naina',
    7 : 'nikita',
    20 : 'mahipal',
}

def checkFunc(dic1):
    for k,v in dic1.items():
        if k >= 1 and k <= 15:
            print(k,v)
checkFunc(dic1)