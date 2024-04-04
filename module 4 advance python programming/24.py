# Que24:-Write a Python class named Circle constructed by a radius and two methods
# which will compute the area and the perimeter of a circle = (c=2*pi*r).area = pi*r*r

class Circle:
    def area(self,r):
        return 3.14*r*r

    def perimeter(self,r):
        return 2*3.14*r
    

obj = Circle()
a_result = obj.area(7)
c_result = obj.perimeter(7)
print(a_result)
print(c_result)