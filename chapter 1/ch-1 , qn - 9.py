a = [3,4,6,-9,10,8,9,30]
k = 10
mid = int((len(a)-1) / 2)
if a[mid] == k:
    print("key is found at index - ",mid)
elif k > a[mid] :
    for i in range(mid+1,len(a)):
        if a[i] == k:
            print("key is found at index value = ",i)
elif k < a[mid]:
    for i in range(0,mid):
        if a[i] == k:
            print("key is found at index value = ", i)
else:
    print("key not found")