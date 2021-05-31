# n = 123   #3 2 1
# digit = n % 10 #3
# n = n // 10 # 12
# digit = n % 10 #2
# n = n// 10  #1
# digit = n % 10 #1
# n = n // 10 #0

# untill n = 0 repeat digit and n//10

n = 123
while n!=0:                 # T, 12=T, 1=T,0=F
    digit = n % 10          # 3, 2, 1
    print(digit)            # 3, 2, 1
    n = n//10               # 12, 1, 0