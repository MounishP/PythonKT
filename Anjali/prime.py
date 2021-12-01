"""
prime - 1,n
6 -> 2,3,4,5
"""
count = 0
for n in range(1, 100):
    for i in range(2, n):
        if n % i == 0:
            count+=1
    else:
        print(n)


