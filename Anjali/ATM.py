count = 0
users = ["Mounish", "Anjali", "Aryan"]
pins = [2223, 4422, 5500]
balances = [20000, 15000, 25000]
balance = 0


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
    balance = balance - amount
    proceed = int(input("Enter your option(1-continue,2-exit): "))
    if proceed == 1:
        menu()
    else:
        close()


def close():
    print("****************************************************")
    print("                                                    ")
    print("---Thank you for using Mounish National bank ATM.---")
    print("                                                    ")
    print("****************************************************")


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


try:
    while count != 3:
        pin = int(input("Enter the pin: "))
        print("")


        def digit(pin):
            temp = pin
            count = 0
            while temp != 0:
                count += 1
                temp = temp // 10

            if count == 4:
                return pin
            else:
                print("Pin should be 4 digits only")


        if digit(pin) in pins:
            # sl = "select sno from users where pin = 'pin'"
            if pin == pins[0]:
                print("Hi ", users[0])
                balance = balances[0]
            elif pin == pins[1]:
                print("Hi ", users[1])
                balance = balances[1]
            else:
                print("Hi ", users[2])
                balance = balances[2]
            menu()
            break
        else:
            print("Incorrect Pin")
            count += 1

except ValueError:
    print("Enter only numbers...")
