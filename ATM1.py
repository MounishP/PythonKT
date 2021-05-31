from time import sleep

users = ['Mounish', 'MyCar', 'Darling']
pins = ['2605', '2223', '1432']
bal = [1000, 6000, 2000]
count = 0

print("-------------------------------")
print("*******************************")
print("========Enter the card=========")
print("*******************************")
print("-------------------------------")
print()
sleep(5)

pin = input("Enter the pin: ")


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


def welcome(n):
    print("***************************************")
    print("*                                     *")
    print(f"*    Welcome {users[n]} to the ATM    *")
    print("*                                     *")
    print("***************************************")
    menu()


def checkPin(pin):
    global count
    flag = True
    while flag:
        count = count + 1
        flag = False
        if count < 3:
            if pin.isdigit() and (pin in pins):
                if pin == pins[0]:
                    n = 0
                    welcome(n)
                    break
                elif pin == pins[1]:
                    n = 1
                    welcome(n)
                    break
                elif pin == pins[2]:
                    n = 2
                    welcome(n)
                    break
            else:
                print("----------------------------------------------")
                print("**********************************************")
                print(f"====== Incorrect pin number ====")
                print("**********************************************")
                print("----------------------------------------------")
                pin = input("Re-Enter the pin: ")
                checkPin(pin)
        else:
            print("*****************************************")
            print("*                                       *")
            print(f"* 3 unsuccessful attempts, card blocked *")
            print("*                                       *")
            print("*****************************************")
            break


checkPin(pin)
