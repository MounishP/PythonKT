"""
Conditional Statements:

1. Simple if
    if.........
2. If....else
    if....else.....
3. elif
    if.....elif.....elif.....else......
4. nested if
    if.....:
        if.....:
            ...
        elif:
            ...
        elif:
            ....
        else:
            ...
    else:
        ....


Input function: ---> String
"""
"""
 Medical care centre:
    Name,Age,Gender
    0 to 18 --> gender is male -- Apollo/ female -- medicare
    19 to 30 --> gender is male -- yasodha/ female -- columbia asia
    31 to 60+ --> gender is male -- care/ female -- kims
   """

name = input("Enter the name: ")
age = int(input("Enter the age: "))
gender = input("Enter the gender: ")

if age > 0 and age <= 18:
    print("visit Apollo")
elif age > 19 and age <= 30:
    print("visit yasodha")
elif age > 31:
    print("Visit Care")
else:
    print("Contact Admin")
