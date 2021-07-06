class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x * other.x


a = A(3)
b = A(4)
c = a + b
print(c)