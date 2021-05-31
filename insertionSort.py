arr = [12, 11, 13, 5, 6]
for i in range(1, len(arr)):         #1,2,3
    key = arr[i]                     #11,13,5
    j = i - 1                        #0,1,2
    while j >= 0 and key < arr[j]:   #True,False,True
        arr[j + 1] = arr[j]          #arr[1] = 12, arr[3] = 13
        j -= 1                       #-1, 1
    arr[j + 1] = key                 #arr[0] = 11, arr[2] = 13
print(arr)
# [11,12,13,5,6]
# [11,12,13,5,6]
#