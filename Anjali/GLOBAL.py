"""
global keyword
1. local variable
2. global variable
"""

b = 3  # global variable


def add():
    a = 5  # local variable for the  function
    global b
    b = b + 5
    print(a)
    print(b)


add()
print(b)
