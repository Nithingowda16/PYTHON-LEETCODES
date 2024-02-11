def merge(arr, start, mid, end, count):
    n1 = mid - start + 1
    n2 = end - mid

    left = arr[start:start + n1]
    right = arr[mid + 1:mid + 1 + n2]

    i = j = 0
    k = start

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            count[0] += (n1 - i)  # Counting the pairs
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr, start, end, count):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid, count)
        merge_sort(arr, mid + 1, end, count)
        merge(arr, start, mid, end, count)

def reverse_pairs(arr):
    count = [0]  # Using a list to simulate passing by reference
    merge_sort(arr, 0, len(arr) - 1, count)
    return count[0]

# Example usage:
arr = [1, 3, 2, 3, 1]
result = reverse_pairs(arr)
print("Number of reverse pairs:", result)
