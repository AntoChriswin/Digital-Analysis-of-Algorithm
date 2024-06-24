def merge_sort(nums1, m, nums2, n):
    result = [0] * (m + n)
    i = j = k = 0

    while i < m and j < n:
        if nums1[i] < nums2[j]:
            result[k] = nums1[i]
            i += 1
        else:
            result[k] = nums2[j]
            j += 1
        k += 1

    while i < m:
        result[k] = nums1[i]
        i += 1
        k += 1

    while j < n:
        result[k] = nums2[j]
        j += 1
        k += 1

    return result

# Example Usage
nums1 = [3, 8, 1, 9]
nums2 = [4, -2, 0, 7]
m = len(nums1)
n = len(nums2)

merged_array = merge_sort(nums1, m, nums2, n)
print(merged_array)
