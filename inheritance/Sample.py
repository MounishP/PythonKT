class Parent:
    def things(self):
        print("Belongs to parent")


class Child(Parent):
    def things(self):
        print("Belong to child")


child = Child()
child.things()

