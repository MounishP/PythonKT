class GrandFather:
    def house(self):
        print("This is Grandfather")


class Father(GrandFather):
    def car(self):
        print("This is Father")


class You(Father):
    def bike(self):
        super().car()
        super().house()
        print("This is child")


father = Father()
father.house()
father.car()

child = You()
child.bike()
child.car()
child.house()
