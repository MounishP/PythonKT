"""
1. input number
2. check n => -ve /+ve
3. if -ve : make +ve -> reverse(n) -> make -ve
4. if +ve: reverse(n)
5. n = 0 -> rev =0
"""

n = int(input("Enter the number: "))


def makePositive(n):
    return n * (-1)


def reverse(n):
    rev = 0
    while n!=0:
        rev = rev * 10 + n%10
        n//=10
    return rev


def makeNegative(rev):
    return rev * (-1)


if n < 0:
    pn = makePositive(n)
    rev = reverse(pn)
    nn = makeNegative(rev)
    print(nn)
else:
    print(reverse(n))