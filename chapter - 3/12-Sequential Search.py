a = [1,2,3,4,5]
n = int(input("enter any number to search :"))
for i in range(len(a)):
    if a[i] == n:
        print("element found :",a[i])
        b = 1
    else:
        b = 0
if b==0:
    print("element not found")