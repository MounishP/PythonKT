l = [12, 11, 13, 5, 6]
for i in range(1, len(l)):         # 1 ,2, 3, 4 O(n)
    key = l[i]                     # 6
    j = i - 1                      # 3
    while j >= 0 and key < l[j]:   # True, True, True, False    O(1)
        l[j+1] = l[j]              # l[4] = 13, l[3] = 12, l[2] = 11
        j = j - 1                  # 2, 1, 0
    l[j + 1] = key                 # l[1] = 6

# [11,12,13,5,6]
# [11,12,13,5,6]
# [5, 11, 12, 13, 6]
# [5, 6, 11, 12, 13]
print(l)

#O(n),O(n)