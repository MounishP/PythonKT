from time import sleep

users = ["Mounish", "Poojitha", "Prakash"]
pins = ["2605", "0707", "0807"]
bal = [10000, 7000, 5000]
ask = 1

print("-------------------------------")
print("*******************************")
print("========Enter the card=========")
print("*******************************")
print("-------------------------------")
print()
sleep(5)


def toContinue():
    print("""
            1. Continue (C)
            2. exit  (E)
    """)
    opt = input("Enter your option: ")
    if opt.capitalize() == 'C':
        menu()
    elif opt.capitalize() == 'E':
        print("---------------------------------------------")
        print("*********************************************")
        print("========Thank you for using our ATM =========")
        print("*********************************************")
        print("---------------------------------------------")
        exit()


def balance():
    print("----------------------------------------------")
    print("**********************************************")
    print(f"====== The current balance in your is {bal} ====")
    print("**********************************************")
    print("----------------------------------------------")
    toContinue()


def withdraw():
    global bal
    withAmt = int(input("Enter the amount to withdraw: "))
    if withAmt > bal:
        print("----------------------------------------------")
        print("**********************************************")
        print(f"============ Insufficient Balance ==========")
        print("**********************************************")
        print("----------------------------------------------")
    else:
        bal = bal - withAmt
        print("----------------------------------------------")
        print("**********************************************")
        print(f"============ Withdrawal Successful ==========")
        print("**********************************************")
        print("----------------------------------------------")
    toContinue()


def deposit():
    global bal
    depAmt = int(input("Enter the amount to deposit: "))
    bal = bal + depAmt
    print("----------------------------------------------")
    print("**********************************************")
    print(f"============ Deposit Successful ==========")
    print("**********************************************")
    print("----------------------------------------------")
    toContinue()


def menu():
    print("""
          1. Check Balance
          2. Withdraw
          3. Deposit
          4. Exit
          """)
    option = int(input("Enter your option: "))
    if option == 1:
        balance()
    elif option == 2:
        withdraw()
    elif option == 3:
        deposit()
    elif option == 4:
        exit()
    else:
        print("======Invalid option========")
        menu()


pin = input("Enter the pin: ")


def checkPin(pin):
    global ask
    while True:
        if ask <= 3:
            if (pin.__len__() == 4) and (pin in pins) and pin.isdigit():
                menu()
            else:
                ask = ask + 1
                print("----------------------------------------------")
                print("**********************************************")
                print("====== Incorrect pin number ====")
                print("**********************************************")
                print("----------------------------------------------")
                pin = input("Re-enter the pin: ")
                checkPin(pin)
        else:
            print("----------------------------------------------")
            print("**********************************************")
            print("====== CARD BLOCKED, 3 UNSUCCESSFUL ATTEMPTS ====")
            print("**********************************************")
            print("----------------------------------------------")
        break


checkPin(pin)
