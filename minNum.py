n = int(input("Enter the number: "))
tax = 0;
l = []
val = input("Enter the value: ").split(" ")
for i in val:
    l.append(int(i))

for j in range(len(l)):
    if l[j] <=1000:
        tax = tax + 0
    else:
        tax = tax + (l[j]-l[0])/10
print(tax)