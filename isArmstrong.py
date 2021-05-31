"""
#When a num is rasied to its length and is totaled then it is armstrong number
153 = 1**3 + 5**3 + 3**3 ==> 153
1634 = 1**4 + 6**4 + 3**4 + 4**4
Steps:
1. input
2. separate the digits
3. length of the number
4. power of num with length
5. sum of powers
6. compare total with num
"""

n = int(input("number: "))    #153


def length(n):          #153
    result = 0          #0
    while n!=0:         #153!=0, 15!=0 , 1!=0,0!=0
        digit = n % 10  #3,5,1
        result += 1     #1,2,3
        n = n//10       #15,1,0
    return result       #3


def isArmstrong(n): #153
    temp = n        #temp = 153
    l = length(n)   #153 -->  3
    total = 0       #0
    while n!=0:     #153!=0,15!=0,1!=0
        digit = n % 10                 #3,5,1
        total = total + pow(digit,l)   # 0+ pow(3,3)->27,27+pow(5,3)->152,152+1->153
        n=n//10                        #15,1,0
    return total == temp #153==153 -->True


print(isArmstrong(n)) #153