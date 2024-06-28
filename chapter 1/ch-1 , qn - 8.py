a = [3, 7, 3, 5, 2, 5, 9, 2]
for i in range(len(a)):
    b = 0
    for j in range(0,len(a)-i-1):
        if a[j] > a[j+1]:
            a[j] , a[j+1] = a[j+1] , a[j]
            b = 1
    if b == 0:
        break
print(a)