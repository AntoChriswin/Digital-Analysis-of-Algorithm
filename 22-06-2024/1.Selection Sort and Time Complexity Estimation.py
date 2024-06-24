import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Test Case A
start_time_A = time.time()
output_A = selection_sort([10, 5, 80, -2, 15, 23, 45])
end_time_A = time.time()
time_taken_A = end_time_A - start_time_A
print(output_A)

# Test Case B
start_time_B = time.time()
output_B = selection_sort([12, 3, 0, 34, -11, 2, 8])
end_time_B = time.time()
time_taken_B = end_time_B - start_time_B
print(output_B)

print("Time taken for Test Case A:", time_taken_A)
print("Time taken for Test Case B:", time_taken_B)
