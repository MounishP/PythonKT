# def marks(name, sanskrit, english, kannada, math, science, social):
#     total = sanskrit+english+kannada+math+science+social
#     print(name," total is: ", total)
#
#
# for i in range(1,11):
#     name = input("Enter the name: ")
#     sanskrit = int(input("Enter marks: "))
#     english = int(input("Enter marks: "))
#     kannada = int(input("Enter marks: "))
#     math = int(input("Enter marks: "))
#     science = int(input("Enter marks: "))
#     social = int(input("Enter marks: "))
#     marks(name,sanskrit,english,kannada,math,science,social)

class Marks:
    def __init__(self, name, sanskrit, english, kannada, maths, science, social):
        self.name = name
        self.sanskrit = sanskrit
        self.english = english
        self.kannada = kannada
        self.maths = maths
        self.science = science
        self.social = social

    def total(self):
        total = self.social + self.science + self.maths + self.kannada + self.english + self.sanskrit
        print(self.name, " scored ", total)


try:
    s1 = Marks("mounish", 92, 90, 86, 100, 94, 90)
    s1.total()
    s2 = Marks("anjali")
except TypeError:
    print("must fill all the fields")
