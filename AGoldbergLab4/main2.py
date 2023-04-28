import random

# Quicksort with first item as pivot
def quicksort_first(arr):
    if len(arr) < 2:
        return arr
    
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if high - low <= 0:
            continue
        pivot = arr[low]
        i, j = low + 1, high
        while i <= j:
            if arr[i] <= pivot:
                i += 1
            elif arr[j] >= pivot:
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        if j - low > 1:
            stack.append((low, j - 1))
        if high - j > 1:
            stack.append((j + 1, high))
    return arr

# Quicksort with first item as pivot, using insertion sort for small partitions
def quicksort_first_insertion_100(arr):
    if len(arr) < 2:
        return arr
    
    if len(arr) <= 100:
        return insertion_sort(arr)
    
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if high - low <= 0:
            continue
        pivot = arr[low]
        i, j = low + 1, high
        while i <= j:
            if arr[i] <= pivot:
                i += 1
            elif arr[j] >= pivot:
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        if j - low > 1:
            stack.append((low, j - 1))
        if high - j > 1:
            stack.append((j + 1, high))
    return arr

# Quicksort with first item as pivot, using insertion sort for smaller partitions
def quicksort_first_insertion_50(arr):
    if len(arr) < 2:
        return arr
    
    if len(arr) <= 50:
        return insertion_sort(arr)
    
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if high - low <= 0:
            continue
        pivot = arr[low]
        i, j = low + 1, high
        while i <= j:
            if arr[i] <= pivot:
                i += 1
            elif arr[j] >= pivot:
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        if j - low > 1:
            stack.append((low, j - 1))
        if high - j > 1:
            stack.append((j + 1, high))
    return arr

# Quicksort with median-of-three as pivot
def quicksort_median(arr):
    if len(arr) < 2:
        return arr
    
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if high - low <= 0:
            continue
        if high - low == 1:
            if arr[low] > arr[high]:
                arr[low], arr[high] = arr[high], arr[