def quicksort_first_pivot_insertion(arr, threshold=100):
    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        return arr if arr[0] <= arr[1] else [arr[1], arr[0]]
    if len(arr) <= threshold:
        return insertion_sort(arr)
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quicksort_first_pivot_insertion(left, threshold) + [pivot] + quicksort_first_pivot_insertion(right, threshold)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current
    return arr