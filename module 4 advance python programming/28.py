# Que28:-What is used to check whether an object o is an instance of class A?

class A():
    def greet(self):
        print("Good Morning")

obj = A()

# if class and object match it will show True else False
print(isinstance(obj, A))