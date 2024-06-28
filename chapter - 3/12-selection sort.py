a = [5,4,1,3,2]
l = len(a)
for i in range(l):
    min = i
    for j in range(i+1,l):
        if a[j] < a[min]:
            min = j
    a[i],a[min] = a[min],a[i]
print(a)