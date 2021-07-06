class Parent:

    def things(self):
        print("Belong to parent")


class Child(Parent):

    def things(self):
        print("Belong to child")


child = Parent()
child.things()