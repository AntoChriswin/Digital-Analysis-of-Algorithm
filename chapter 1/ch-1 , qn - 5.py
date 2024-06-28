n = [1, 2, 3, 4, 5]
max = n[0]
for i in range(len(n)):
    if n[i] > max:
        max = n[i]

print("max = ",max)
