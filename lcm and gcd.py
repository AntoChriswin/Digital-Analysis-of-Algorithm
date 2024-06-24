n1 = int(input("enter a number : "))
n2 = int(input("enter a number : "))
i = 1
while((i<=n1) and (i<=n2)):
    if(n1%i==0 and n2%i == 0):
        gcd = i
    i+=1
lcm = (n1*n2)/gcd
print("gcd = ",gcd)
print("lcm = ",lcm)