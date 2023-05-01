import os
import glob

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def quick_sort(arr, left, right, count_dict):
    if left >= right:
        return

    mid = (left + right) // 2
    pivot = arr[mid]

    i = left
    j = right
    while i <= j:
        count_dict['comparisons'] += 1
        while arr[i] < pivot:
            count_dict['comparisons'] += 1
            i += 1

        count_dict['comparisons'] += 1
        while arr[j] > pivot:
            count_dict['comparisons'] += 1
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            count_dict['exchanges'] += 1
            i += 1
            j -= 1

    quick_sort(arr, left, j, count_dict)
    quick_sort(arr, i, right, count_dict)


def sort_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        data = None
        for line in lines:
            for num in line.strip().split():
                if data is None:
                    data = LinkedListNode(int(num))
                    curr = data
                else:
                    curr.next = LinkedListNode(int(num))
                    curr = curr.next

        # Convert linked list to list
        arr = []
        curr = data
        while curr is not None:
            arr.append(curr.data)
            curr = curr.next

        # Perform quicksort
        count_dict = {'comparisons': 0, 'exchanges': 0}
        quick_sort(arr, 0, len(arr) - 1, count_dict)

        return arr, count_dict

def main():
    input_dirs = ['./50input', './bigInput']
    output_dir = './median3Output'
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

    for input_dir in input_dirs:
        input_files = glob.glob(input_dir + '/*.dat')
        for input_file in input_files:
            sorted_arr, count_dict = sort_file(input_file)
            output_file = os.path.join(output_dir, 'Output' + os.path.basename(input_file))
            with open(output_file, 'w') as f:
                if input_dir == './50input':
                    for item in sorted_arr:
                        f.write(str(item) + '\n')
                f.write(f"Comparisons: {count_dict['comparisons']}, Exchanges: {count_dict['exchanges']}\n")

if __name__ == '__main__':
    main()
