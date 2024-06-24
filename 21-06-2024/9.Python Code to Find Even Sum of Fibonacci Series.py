def even_fibonacci_sum(n):
    a, b = 0, 1
    total_sum = 0

    for _ in range(n):
        if a % 2 == 0:
            total_sum += a
        a, b = b, a + b

    return total_sum

n = 4
print("Sum of even Fibonacci numbers till the", n, "th term:", even_fibonacci_sum(4))
