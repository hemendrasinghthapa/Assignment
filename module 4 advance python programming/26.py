# Que25:-Explain Inheritance in Python with an example? What is init? Or What
# Is A Constructor In Python?

# Ans:-

# Inheritance is use to reuse code and methods from different classes
# __init__ is a constructor in python

class Tree:
    def leaves(self):
        print("Leaves")

class Fruit(Tree):
    def leaves(self):
        print("Strawberry")

obj = Fruit()
obj.leaves()