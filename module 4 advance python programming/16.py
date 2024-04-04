# Que16:- Can one block of except statements handle multiple exception?

# Ans:-
'''
Yes, a single block of except statements can handle multiple exceptions in Python.
You can specify multiple exception types within the same except block by enclosing 
them in parentheses and separating them with commas.
'''

try:
    # Code that might raise an exception
    pass
except (ValueError, TypeError):
    # Exception handling code
    pass