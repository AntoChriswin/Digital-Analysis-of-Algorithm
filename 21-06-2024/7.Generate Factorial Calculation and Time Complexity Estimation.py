import time

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

# Testing the factorial function
test_cases = [4, -3, 6]
for num in test_cases:
    if num < 0:
        print(f"Factorial calculation for {num}: No negative value allowed.")
    else:
        start_time = time.time()
        result = factorial(num)
        end_time = time.time()
        print(f"Factorial calculation for {num}: Value is {result}")
        print(f"Time taken for calculation: {end_time - start_time} seconds")
