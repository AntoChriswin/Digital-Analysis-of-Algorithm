a = [5, 2, 9, 1, 5, 6]
for i in range(len(a)):
    min = i
    for j in range(i+1,len(a)):
        if a[j] < a[min]:
            min = j
    a[min] , a[i] = a[i] , a[min]
print(a)