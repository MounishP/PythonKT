n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if n % 1 == 0 and n % n == 0:
        print(f"{n} is prime.")
