a =  [7,2,1,3,5,6,100]
if a[0] > a[0+1]:
    print("index",0,"is greater than its neighbors ")
    exit()
elif a[len(a)-1] > a[len(a)-2]:
    print("index",len(a)-1,"is greater than its neighbors ")
    exit()
for i in range(1,len(a)-1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        print("index",i,"is greater than its neighbors ")
        break

  