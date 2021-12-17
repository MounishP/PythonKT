from functools import reduce


def addsumm(n, m):
    return n + m  # 23+21 = 44,44+45=89,89+98=187


x = reduce(addsumm, [23, 21, 45, 98, 76, 76])
print(x)
