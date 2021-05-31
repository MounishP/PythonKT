n = int(input("Enter the number: "))


def fact(n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i
    # print(ans)
    return ans


def isStrong(n):
    temp = n
    sum = 0
    while n != 0:
        digit = n % 10
        sum = sum + fact(digit)
        n //= 10

    if temp == sum:
        return True
    return False


print(isStrong(n))
