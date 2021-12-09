#  -b + sqrt(b*b - 4ac)/2a
import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a != 0:
    if b * b > 4 * a * c:
        print("roots are real")
        x1 = -b + math.sqrt(b * b - 4 * a * c)
        x2 = -b - math.sqrt(b * b - 4 * a * c)
        print("Roots are: ", x1, ",", x2)
    else:
        print("Roots are Imaginary")
else:
    print("'a' should not be 0")
