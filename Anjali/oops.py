"""
OOP -> Object oriented programming
Class -> is a blueprint
Object -> instance of the class
4 pillars of oops
Inheritance -> the ability to get or take features from ur parent class.
polymorphism -> poly= many,forms -> one entity exhibiting many forms
abstraction -> hiding all the complex part and showing only how much it is necessary/easy.
encapsulation -> binding things into a single entity.

Method -> is a function which is written inside a class.
"""


class MyClass:
    x = 5

    def myFunc(self):
        print("function is now a method",self.x)


myClass = MyClass()
print(myClass.x)
myClass.myFunc()

myClass1 = MyClass()
print(myClass1.x)
