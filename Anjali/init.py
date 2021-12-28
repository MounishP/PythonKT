"""
init-> __init__() special function, need not to be called
if an object is created its calls the init function
Constructor == init()
"""


class Student:
    def __init__(mounish, name, age):
        mounish.name = name
        mounish.age = age

    def names(mounish):
        print("Student name is " + mounish.name)


s1 = Student("Anjali", 25)
s1.names()
s2 = Student("Aryan",24)
s2.names()
