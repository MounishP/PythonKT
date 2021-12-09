"""
Tuple- used to store multiple data in a single variable
represented by ()
ordered
unchangeable
allows duplicates
"""

t = (1, 2, 2, 3, 4, 5, 6, 6, 7)  # account no, pan no
# t[2] = 99
l = list(t)
t1 = tuple(l)
# print(t1)

for i in t:
    print(i)
