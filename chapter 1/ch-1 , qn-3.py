def subarr(a):
    l = len(a)
    arr = []
    for i in range(l):
        for j in range(i+1,l+1):
            arr.append(a[i:j])

    return arr
def dist(a):
    l = len(set(a))
    return l**2

n = [10,1,2,7,6,1,5]
a = subarr(n)
print(a)
s = 0
for i in range(len(a)):
    b = dist(a[i])
    s = s+b

print(s)
