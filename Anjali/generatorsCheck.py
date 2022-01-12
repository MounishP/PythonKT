"""
Generator -> will allow us to return multiple statements from the function
"""

a = 4
b = 5
c = 7


def add(a, b, c):
    yield a + b
    yield a + c


x = add(a, b, c)
print(x.__next__())
print(x.__next__())
