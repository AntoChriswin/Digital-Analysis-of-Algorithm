def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

a = [1, 2, 3,2, 3, 4]
print(a)
print(merge_sort(a))
