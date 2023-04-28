import random
import time
from typing import List, Tuple, Callable
import os


def insertion_sort(arr: List[int], left: int, right: int):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def quicksort_first(arr: List[int], left: int, right: int):
    if right - left <= 1:
        if arr[right] < arr[left]:
            arr[left], arr[right] = arr[right], arr[left]
        return
    pivot = arr[left]
    i = left + 1
    j = right
    while True:
        while i <= j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[left], arr[j] = arr[j], arr[left]
    quicksort_first(arr, left, j - 1)
    quicksort_first(arr, j + 1, right)

def quicksort_first_insertion(arr: List[int], left: int, right: int, threshold: int):
    if right - left <= 1:
        if arr[right] < arr[left]:
            arr[left], arr[right] = arr[right], arr[left]
        return
    if right - left + 1 <= threshold:
        insertion_sort(arr, left, right)
        return
    pivot = arr[left]
    i = left + 1
    j = right
    while True:
        while i <= j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[left], arr[j] = arr[j], arr[left]
    quicksort_first_insertion(arr, left, j - 1, threshold)
    quicksort_first_insertion(arr, j + 1, right, threshold)

def quicksort_median(arr: List[int], left: int, right: int):
    if right - left <= 1:
        if arr[right] < arr[left]:
            arr[left], arr[right] = arr[right], arr[left]
        return
    mid = (left + right) // 2
    if arr[left] > arr[mid]:
        arr[left], arr[mid] = arr[mid], arr[left]
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[mid] > arr[right]:
        arr[mid], arr[right] = arr[right], arr[mid]
    pivot = arr[mid]
    arr[mid], arr[right] = arr[right], arr[mid]
    i = left
    j = right - 1
    while True:
        while i <= j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[right], arr[i] = arr[i], arr[right]
    quicksort_median(arr, left, i - 1)
    quicksort_median(arr, i + 1, right)

def natural_merge_sort(arr: List[int]) -> List[int]:
    # Define a helper function to merge two sorted lists
    def merge(left: List[int], right: List[int]) -> List[int]:
        merged = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        if i < len(left):
            merged.extend(left[i:])
        if j < len(right):
            merged.extend(right[j:])
        return merged

    if len(arr) <= 1:
        return arr

    run_starts = []
    run_start = 0
    increasing = True
    for i in range(1, len(arr)):
        if (increasing and arr[i] < arr[i - 1]) or (not increasing and arr[i] > arr[i - 1]):
            run_starts.append(run_start)
            run_start = i
            increasing = not increasing

    run_starts.append(run_start)
    run_starts.append(len(arr))

    while len(run_starts) > 2:
        new_run_starts = []

        for i in range(0, len(run_starts) - 2, 2):
            left = arr[run_starts[i]:run_starts[i + 1]]
            right = arr[run_starts[i + 1]:run_starts[i + 2]]
            merged = merge(left, right)
            arr[run_starts[i]:run_starts[i + 2]] = merged
            new_run_starts.append(run_starts[i])

        if len(run_starts) % 2 == 1:
            last_run = arr[run_starts[-2]:run_starts[-1]]
            arr[run_starts[-2]:] = last_run
            new_run_starts.append(run_starts[-2])

        run_starts = new_run_starts + [len(arr)]

    return arr

def load_data(file_name):
    with open(file_name, 'r') as f:
        data = []
        for line in f:
            # split the line into a list of strings using whitespace as the delimiter
            values = line.strip().split()
            # convert each string to an integer using a list comprehension
            integers = [int(value) for value in values]
            # add the list of integers to the data list
            data.extend(integers)
    return data

def save_data(file_name: str, data: List[int]):
    with open(file_name, 'w') as f:
        f.write('\n'.join(str(x) for x in data))

def run_sorts(file_name: str, sort_functions: List[Tuple[str, Callable]]):
    data = load_data(file_name)
    for sort_name, sort_function in sort_functions:
        sorted_data = data.copy()
        start_time = time.time()
        sort_function(sorted_data)
        elapsed_time = time.time() - start_time
        print(f"{sort_name} on {file_name}: {elapsed_time:.4f} seconds")
        save_data(f"{file_name}_{sort_name}_output.txt", sorted_data)

def main():
    sort_functions = [
        ("quicksort_first", lambda arr: quicksort_first(arr, 0, len(arr) - 1)),
        ("quicksort_first_100", lambda arr: quicksort_first_insertion(arr, 0, len(arr) - 1, 100)),
        ("quicksort_first_50", lambda arr: quicksort_first_insertion(arr, 0, len(arr) - 1, 50)),
        ("quicksort_median", lambda arr: quicksort_median(arr, 0, len(arr) - 1)),
        ("natural_merge_sort", natural_merge_sort)
    ]


    folder_path = "50input"
    file_names = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".dat")]


    for file_name in file_names:
        run_sorts(file_name, sort_functions)

if __name__ == "__main__":
    main()
