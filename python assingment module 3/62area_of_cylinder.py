# Que62:- Write a Python program to calculate surface volume and area of a
# cylinder

# Ans:-
radius = float(input("Enter the radius:"))
height = float(input("Enter the height:"))

surface_area = 2 * 3.14 * radius * (radius + height)

volume = 3.14 * radius ** 2 * height

print("Area of the Cylinder:", surface_area)
print("Volume of the Cylinder:", volume)
