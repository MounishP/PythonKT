"""
method Over loading ->

multiple methods having same name with different args
"""
from multipledispatch import dispatch


@dispatch(int, int)
def product(a, b):
    print(a * b)


@dispatch(float, float, float)
def product(a, b, c):
    print(a * b * c)


@dispatch(int, float)
def product(a, b):
    print(a * b)


@dispatch(int, str)
def product(a, b):
    print(a * b)


product(2, 3)
product(1.2, 2.2, 3.3)
product(2, 3.5)
product(3, 'mounish')
