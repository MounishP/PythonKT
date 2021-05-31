l= [2, 5, 6, 78, 4, 6, 7, 2, 3, 1]
start = 3
end = 7
newList = l[start:end + 1]
newList.reverse()
for i in range(start, end+1):
    l[i] = newList[i-start]
print(l)
