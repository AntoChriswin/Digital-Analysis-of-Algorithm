
def ispal(a):
    if (a == a[::-1]):
        return 1
    else:
        return 0



w = ["abc","car","racecar","cool"]
for i in range(len(w)):
    a = ispal(w[i])
    if a == 1:
        print(w[i],"is a palindrome")
        break

if a == 0:
    print(" ")
