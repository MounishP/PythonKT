n = int(input("Enter the number: "))


def reverse(num):
    rev = 0
    while num != 0:
        rev = rev * 10 + (num % 10)
        num = num // 10

    return rev


def isPalindrome(num):
    return num == reverse(num)


print(isPalindrome(n))
