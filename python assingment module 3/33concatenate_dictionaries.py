# Que33:- Write a Python script to concatenate following dictionaries to create a
# new one.

# Ans:-

d1 = {
    1 :'nit',
    2 :'gujar',
}
d2= {
    3 :'kamal',
    4 :'sharma',
}

d3 = {}
d1.update(d2)

print(d1)