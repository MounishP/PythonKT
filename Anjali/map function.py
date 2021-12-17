"""
map function -> map ur variables to a function

Set ->
"""


def squares(n):
    return n * n


x = map(squares, [76, 1, 2, 3, 4, 8, 8])  # 1,4,9,16
print(set(x))
