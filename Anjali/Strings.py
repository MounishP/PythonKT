"""
Strings -> anything which is enclosed in a single or double "'
Strings have indexs
String is a non-primitive data type
len() -> is a function which gives you the length of the string

'mounish'
'this is a python class'
'123456789'
'!@#$%^&*()'

"""

# indexing

# name = input("Enter the name: ")
# # print(name[4])
# # print(len(name))
#
# for i in range(0, len(name)):
#     print(name[i])

"""
m
mo
mou
moun
mouni
mounis
mounish
"""

# Spilting of Str

fruit = "apple"
check = "pp"
print(check in fruit)

"""
original = "ababa"
check = "babaa" 

ababa == babaa
babaa == babaa --> True
abaab
baaba
aabab
"""

"""
ababaababa
"""

org = "ababa"
check = "babaa"

org1 = org + org
if check in org1:
    True
else:
    False
