def isEven(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


n = int(input("Enter a number: "))
print(isEven(n))
