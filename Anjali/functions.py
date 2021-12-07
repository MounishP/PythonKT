"""
Function -> it is a block of code
why?
    1. Code reusability
"""
x = 98
y = 98


def add(a, b):  # function definition
    return a + b


# print(add(x, y))  # function call
add(7, 3)
add(9, 89)
add(67, 45)

"""
expenses = house rent (maid+electricity+water)
"""




# shoes = int(input("Enter the shoes amount: "))
# clothes = int(input("Enter the clothes amount: "))
# food = int(input("Enter the food amount: "))


def houseRent(maid, ele, water, rent):
    return maid + ele + water + rent


def shopping(shoes, clothes, food):
    return shoes + clothes + food


# expenses = houseRent(maid, ele, water, rent) + shopping(shoes, clothes, food)
# print(expenses)
# print(shopping(shoes,clothes,food))

# count = 0
# sum = 0
# while count < 3:
#     print(count)
#     maid = int(input("Enter the maid amount: "))
#     ele = int(input("Enter the ele amount: "))
#     water = int(input("Enter the water amount: "))
#     rent = int(input("Enter the rent amount: "))
#
#     sum = sum + houseRent(maid, ele, water, rent)
#     count += 1
#
#
# print(sum)



pin_original = 1234
count = 1
pin = int(input("enter the pin: "))
while count < 3:
    if pin == pin_original:
        print("welcome to my atm")
        break
    else:
        count+=1
        pin = int(input("enter the pin: "))
