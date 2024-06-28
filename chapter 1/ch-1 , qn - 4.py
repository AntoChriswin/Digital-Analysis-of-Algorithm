a = [1,2,3,4]
k = 1
s = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            b = i*j
            if b%k == 0:
                s = s+1
print(s)
        