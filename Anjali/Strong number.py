"""
Strong number -> 145 - 1! + 4! + 5! = 145
1. take input
2. separate the digits
3. find factorial of the digits
4. sum of factorials
5. compare with given number
"""

n = int(input("Enter the number: "))
temp = n
total = 0


def fact(digit):
    prod = 1
    for i in range(1, digit+1):
        prod = prod * i

    # print(prod)
    return prod


while n != 0:
    digit = n % 10
    # print(digit,"this is digit")
    total = total + fact(digit)
    # print(total)
    n = n // 10
    # print(n)

print(total == temp)
