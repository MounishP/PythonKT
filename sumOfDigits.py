n = 23487654345675445678765  # 2+3+4
sum = 0
while n != 0:         #234=T, 23=T, 2=T, 0=F
    digit = n % 10    #4 , 3, 2
    sum = sum + digit #0+4=4, 4+3=7, 7+2 =9
    n = n//10         #23,2, 0

print(sum)          #9
