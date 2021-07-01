class Father:
    def house(self):
        print("This is Father")


class Prakash(Father):
    def boy(self):
        print("This is Prakash")


class Renuka(Father):
    def girl(self):
        super().house()
        print("This is Renuka")


boy = Prakash()
boy.boy()
boy.house()

girl = Renuka()
girl.girl()
girl.house()

