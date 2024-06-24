n = int(input("enter any number : "))
s = 0
for i in range(1,n):
    if n%i == 0:
        s = s+i
if s==n:
    print("its a perfect number")
else:
    print("its not a perfect number")