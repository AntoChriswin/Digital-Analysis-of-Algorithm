def find_sum_diff(arr, M, N):
    if M <= 0 or N <= 0 or M > len(arr) or N > len(arr) or M == N:
        return "Illegal input"

    arr.sort()
    mth_max = arr[-M] if M > 0 else None
    nth_min = arr[N - 1] if N > 0 else None

    if mth_max is None or nth_min is None:
        return "Illegal input"

    return mth_max + nth_min, mth_max - nth_min

# Test Cases
test_cases = [
    ([16, 16, 16, 16, 16], 0, 1),
    ([0, 0, 0, 0], 1, 2),
    ([-12, -78, -35, -42, -85], 3, 3),
    ([15, 19, 34, 56, 12], 6, -3),
    ([85, 45, 65, 75, 95], 5, 2)
]

for idx, (arr, M, N) in enumerate(test_cases):
    result = find_sum_diff(arr, M, N)
    print(f"Test Case {idx + 1}: {result}")
