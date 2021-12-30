"""
Child(Sub-class) class acquiring the properties or features of the parent(Super)
 class is called as inheritance.
"""


class Parent:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def printDetails(self):
        print(self.name)
        print(self.gender)


#
# father = Parent("Ratnam", "male")
# mother = Parent("Chandrakala", "female")
# father.printParent()
# mother.printParent()

class Child(Parent):
   pass

child = Child()
child.printDetails()
