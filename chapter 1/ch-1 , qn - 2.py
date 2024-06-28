n1 = [4,3,2,3,1]
n2 = [2,2,5,2,3,6]
s1 = 0
s2 = 0
for i in range(len(n1)):
    if n1[i] in n2 :
        s1 = s1+1
for j in range(len(n2)):
    if n2[j] in n1:
        s2 = s2+1
s3 = [s1,s2]
print(s3)
                                                                                                                    4