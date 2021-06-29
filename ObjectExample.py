class Human:

    def __init__(self, name, age):
        self.name = name   # self = o --> name = p
        self.age = age     # self = o age = 24
        print("Constructor")

    def display(self):
        print("display method")
        print(self.name)
        print(self.age)


