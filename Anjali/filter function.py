def check(l):
    if l >= 5:
        return l


x = filter(check, [12, 3, 45, 6, 7, 8, 9, 8, 76, 5, 4, 3, 2])
print(list(x))
