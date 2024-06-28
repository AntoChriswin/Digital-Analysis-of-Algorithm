a = [1,2,3,4]
b = []
c = []
k = 2
max = max(a)
for i in range(1,max+k+1):
    b.append(i)
for i in range(len(b)):
    if b[i] not in a:
        c.append(b[i])
print(k,"th missing positive integer is",c[k-1])