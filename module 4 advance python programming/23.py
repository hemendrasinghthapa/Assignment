# Que23:-Write a Python class named Rectangle constructed by a length and width and a method
#  which will compute the area of a rectangle

class Rectangle:
    def area(self,l,b):
        return l*b
    

r = Rectangle()
result = r.area(5,6)
print(result)