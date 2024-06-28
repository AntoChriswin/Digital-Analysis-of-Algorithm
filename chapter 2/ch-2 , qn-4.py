a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
l = len(a)
for i in range(1,l):
    key = a[i]
    j = i-1
    while j >= 0 and key < a[j]:
        a[j+1] = a[j]
        j = j-1
    a[j+1] = key
print(a)