class Father:
    def money(self):
        print("This is Father")


class Mother:
    def love(self):
        print("This is Mother")


class Child(Father, Mother):
    def spend(self):
        print("This is child")


child = Child()
child.money()
child.love()
child.spend()
