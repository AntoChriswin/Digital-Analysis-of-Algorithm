a = [5,4,1,3,2]
l = len(a)
for i in range(l):
    b = 1
    for j in range(0,l-i-1):
        if a[j] > a[j+1]:
            a[j] , a[j+1] = a[j+1] , a[j]
            b = 0
    if (b==1):
        break
print(a[len(a)-1])
