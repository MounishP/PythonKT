"""
Strong number -> 145 - 1! + 4! + 5! = 145
1. take input
2. separate the digits
3. find factorial of the digits
4. sum of factorials
5. compare with given number
"""

n = int(input("Enter the number: "))
# separate the digit - digit


digit = 4
fact = 1
for i in range(1,digit+1):
    fact = fact * i

print(fact)

#sum of factorials

#check