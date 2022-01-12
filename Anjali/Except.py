"""
Exception handling -> you get errors
"""

try:
    a = int(input("a:"))
    b = int(input("b:"))
    print(a / b)
except ValueError:
    print("enter only integers")
except ZeroDivisionError:
    print("b value must not be 0")
except Exception:
    print("error occured")
