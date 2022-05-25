ar = [9, 3, 1, 2, 8, 4]
temp = 0
print(ar)
for i in range(0, len(ar)-1):
    for j in range(0, len(ar)-1):
        if ar[j] > ar[j+1]:
            temp = ar[j]
            ar[j] = ar[j+1]
            ar[j+1] = temp

print(ar)