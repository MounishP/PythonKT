# class Father:
#     def house(self):
#         print("This is Father")
#
#
# class Prakash(Father):
#     def boy(self):
#         print("This is Prakash")
#
#
# class Renuka(Father):
#     def girl(self):
#         super().house()
#         print("This is Renuka")
#
#
# boy = Prakash()
# boy.boy()
# boy.house()
#
# girl = Renuka()
# girl.girl()
# girl.house()
#
#
# class A:
#     def __init__(self, a):
#         self.a = a
#
#     def __add__(self, other):
#         s = self.a * other.a
#         return s
#
#
# a = A(1)
# b = A(3)
# print(a + b)
#
# def method(a, b):
#     return a + b
#
# 
# def method(a, b, c):
#     return a + b + c
#
#
# print(method(1, 2, 3))
