# import random
# import time
# from typing import List, Tuple, Callable

# def insertion_sort(arr: List[int], left: int, right: int):
#     for i in range(left + 1, right + 1):
#         j = i
#         while j > left and arr[j] < arr[j - 1]:
#             arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             j -= 1

# def quicksort_first(arr: List[int], left: int, right: int):
#     if right - left <= 1:
#         if arr[right] < arr[left]:
#             arr[left], arr[right] = arr[right], arr[left]
#         return
#     pivot = arr[left]
#     i = left + 1
#     j = right
#     while True:
#         while i <= j and arr[i] < pivot:
#             i += 1
#         while i <= j and arr[j] >= pivot:
#             j -= 1
#         if i <= j:
#             arr[i], arr[j] = arr[j], arr[i]
#         else:
#             break
#     arr[left], arr[j] = arr[j], arr[left]
#     quicksort_first(arr, left, j - 1)
#     quicksort_first(arr, j + 1, right)

# def quicksort_first_insertion(arr: List[int], left: int, right: int, threshold: int):
#     if right - left <= 1:
#         if arr[right] < arr[left]:
#             arr[left], arr[right] = arr[right], arr[left]
#         return
#     if right - left + 1 <= threshold:
#         insertion_sort(arr, left, right)
#         return
#     pivot = arr[left]
#     i = left + 1
#     j = right
#     while True:
#         while i <= j and arr[i] < pivot:
#             i += 1
#         while i <= j and arr[j] >= pivot:
#             j -= 1
#         if i <= j:
#             arr[i], arr[j] = arr[j], arr[i]
#         else:
#             break
#     arr[left], arr[j] = arr[j], arr[left]
#     quicksort_first_insertion(arr, left, j - 1, threshold)
#     quicksort_first_insertion(arr, j + 1, right, threshold)

# def quicksort_median(arr: List[int], left: int, right: int):
#     if right - left <= 1:
#         if arr[right] < arr[left]:
#             arr[left], arr[right] = arr[right], arr[left]
#         return
#     mid = (left + right) // 2
#     if arr[left] > arr[mid]:
#         arr[left], arr[mid] = arr[mid], arr[left]
#     if arr[left] > arr[right]:
#         arr[left], arr[right] = arr[right], arr[left]
#     if arr[mid] > arr[right]:
#         arr[mid], arr[right] = arr[right], arr[mid]
#     pivot = arr[mid]
#     arr[mid], arr[right] = arr[right], arr[mid]
#     i = left
#     j = right - 1
#     while True:
#         while i <= j and arr[i] < pivot:
#             i += 1
#         while i <= j and arr[j] >= pivot:
#             j -= 1
#         if i <= j:
#             arr[i], arr[j] = arr[j], arr[i]
#         else:
#             break
#     arr[right], arr[i] = arr[i], arr[right]
#     quicksort_median(arr, left, i - 1)
#     quicksort_median(arr, i + 1, right)

# def natural_merge_sort(arr: List[int]) -> List[int]:
#     # Define a helper function to merge two sorted lists
#     def merge(left: List[int], right: List[int]) -> List[int]:
#         merged = []
#         i, j = 0, 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 merged.append(left[i])
#                 i += 1
#             else:
#                 merged.append(right[j])
#                 j += 1
#         if i < len(left):
#             merged.extend(left[i:])
#         if j < len(right):
#             merged.extend(right[j:])
#         return merged

#     if len(arr) <= 1:
#         return arr

#     run_starts = []
#     run_start = 0
#     increasing = True
#     for i in range(1, len(arr)):
#         if (increasing and arr[i] < arr[i - 1]) or (not increasing and arr[i] > arr[i - 1]):
#             run_starts.append(run_start)
#             run_start = i
#             increasing = not increasing

#     run_starts.append(run_start)
#     run_starts.append(len(arr))

#     while len(run_starts) > 2:
#         new_run_starts = []

#         for i in range(0, len(run_starts) - 2, 2):
#             left = arr[run_starts[i]:run_starts[i + 1]]
#             right = arr[run_starts[i + 1]:run_starts[i + 2]]
#             merged = merge(left, right)
#             arr[run_starts[i]:run_starts[i + 2]] = merged
#             new_run_starts.append(run_starts[i])

#         if len(run_starts) % 2 == 1:
#             last_run = arr[run_starts[-2]:run_starts[-1]]
#             arr[run_starts[-2]:] = last_run
#             new_run_starts.append(run_starts[-2])

#         run_starts = new_run_starts + [len(arr)]

#     return arr

# def load_data(file_name: str) -> List[int]:
#     with open(file_name, 'r') as f:
#         data = [int(line.strip()) for line in f.readlines()]
#     return data

# def save_data(file_name: str, data: List[int]):
#     with open(file_name, 'w') as f:
#         f.write('\n'.join(str(x) for x in data))

# def run_sorts(file_name: str, *sort_functions):
#     data = load_data(file_name)
#     for sort_function in sort_functions:
#         sorted_data = data.copy()
#         sort_name = sort_function.__name__
#         start_time = time.time()
#         sort_function(sorted_data)
#         elapsed_time = time.time() - start_time
#         print(f"{sort_name} on {file_name}: {elapsed_time:.4f} seconds")
#         save_data(f"{file_name}_{sort_name}_output.txt", sorted_data)

# def main():
#     sort_functions = [
#         ("quicksort_first", lambda arr: quicksort_first(arr, 0, len(arr) - 1)),
#         ("quicksort_first_100", lambda arr: quicksort_first_insertion(arr, 0, len(arr) - 1, 100)),
#         ("quicksort_first_50", lambda arr: quicksort_first_insertion(arr, 0, len(arr) - 1, 50)),
#         ("quicksort_median", lambda arr: quicksort_median(arr, 0, len(arr) - 1)),
#         ("natural_merge_sort", natural_merge_sort)
#     ]

#     file_names = [
#         "random_50.txt", "reversed_50.txt", "ordered_50.txt",
#         "random_1000.txt", "reversed_1000.txt", "ordered_1000.txt",
#         "random_2000.txt", "reversed_2000.txt", "ordered_2000.txt",
#         "random_5000.txt", "reversed_5000.txt", "ordered_5000.txt",
#         "random_10000.txt", "reversed_10000.txt", "ordered_10000.txt"
#     ]

#     for file_name in file_names:
#         run_sorts(file_name, sort_functions)

# if __name__ == "__main__":
#     main()

import os
import subprocess
import time

# define the directory where the input files are located
input_dir = "50input"

# define the directory where the output files will be saved
output_dir = "output"

# define the list of sort files to run
# sort_files = ["50orLess.py", "median3.py", "quickSortFirstPivot.py", "quickSortFirstPivotInsert.py"]
sort_files = ["quickSortFirstPivot.py"]

# define the command template to run each sort file
command_template = "python3 {} {}"

# loop through the input files and run each sort file on each input file
for filename in os.listdir(input_dir):
    if not filename.endswith(".dat"):
        # skip non-data files
        continue
    input_file = os.path.join(input_dir, filename)
    print("Processing input file:", input_file)
    for sort_file in sort_files:
        command = command_template.format(sort_file, input_file)
        print("Running command:", command)
        try:
            start_time = time.time()
            subprocess.run(command, shell=True, check=True)
            end_time = time.time()
            print("Ran {} on {} in {:.3f} seconds".format(sort_file, filename, end_time - start_time))
        except subprocess.CalledProcessError as e:
            print("Error running command:", command)
            print("Error message:", e)
