count = 0
originalPin = 1234
balance = 10000


def showBalance():
    print("Balance is ", balance)
    proceed = int(input("Enter your option(1-continue,2-exit): "))
    if proceed == 1:
        menu()
    else:
        close()


def deposit():
    global balance
    amount = int(input("Enter the amount you need to deposit: "))
    balance = balance + amount
    proceed = int(input("Enter your option(1-continue,2-exit): "))
    if proceed == 1:
        menu()
    else:
        close()


def withdraw():
    global balance
    amount = int(input("Enter the amount to withdraw: "))
    balance = balance -amount
    proceed = int(input("Enter your option(1-continue,2-exit): "))
    if proceed == 1:
        menu()
    else:
        close()


def close():
    print("in close")


def menu():
    option = int(input("Enter your option(1-show balance,2-deposit,3-withdraw,4-exit): "))
    if option == 1:
        showBalance()
    elif option == 2:
        deposit()
    elif option == 3:
        withdraw()
    elif option == 4:
        close()


while count != 3:
    pin = int(input("Enter the pin: "))
    if pin == originalPin:
        menu()
        break
    else:
        print("Incorrect Pin")
        count += 1
