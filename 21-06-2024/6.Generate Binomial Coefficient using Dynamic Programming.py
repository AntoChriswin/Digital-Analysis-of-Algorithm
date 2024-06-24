def binomial_coefficient(n, k):
    if k == 0 or n == k:
        return 1
    return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

n = 8
k = 8
result = binomial_coefficient(n, k)
print(f"Binomial Coefficient for n={n}, k={k} is: {result}")
