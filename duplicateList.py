l = [3, 67, 4, 5, 7, 8, 6, 776, 21]

for i in range(len(l) - 2):                # O(n)
    for j in range(i + 1, len(l) - 1):     # O(n)
        if l[i] > l[j]:                    # O(1/n)
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print(l)

# O(n**2), O(n)