import time

def linear_search(arr, key):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == key:
            end_time = time.time()
            return f"Element found in position {i}, Time taken: {end_time - start_time} seconds"
    end_time = time.time()
    return "Not Found, Time taken: {end_time - start_time} seconds"

# Input/Output Series
A = [56, 89, 7, 13, 75, 23, 8, 12]
B = [89, 45, -23, 45, 0, 44, 2]
C = [45, 67, 56, 'A', 34, -2, 100]

key_A = 75
key_B = 0
key_C = 90

print(linear_search(A, key_A))
print(linear_search(B, key_B))
print(linear_search(C, key_C))
