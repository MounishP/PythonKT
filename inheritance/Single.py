class Parent:
    def __init__(self):
        print("This is Parent")

    def property(self):
        print("Belong to parent")


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("This is child")

    def things(self):
        print("Belong to child")


child = Child()
