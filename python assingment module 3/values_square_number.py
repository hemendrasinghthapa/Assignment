'''Que :- Write a Python program to generate and print a list of first and last 5
          elements where the values are square of numbers between 1 and 30.'''
# Ans:-

# num = int(input("enter a number : "))

# Generate a list of squares of numbers between 1 and 30
squares_list = [i ** 2 for i in range(1, 31)]

# Print the entire list
print("List of squares of numbers between 1 and 30:")
print(squares_list)

# Print the first 5 elements
print("\nFirst 5 elements:")
print(squares_list[:5])

# Print the last 5 elements
print("\nLast 5 elements:")
print(squares_list[-5:])
