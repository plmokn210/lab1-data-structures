# import os
# import glob

# class LinkedListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def partition(head, pivot, count_dict):
#     left_head = LinkedListNode(None)
#     right_head = LinkedListNode(None)
#     left_curr = left_head
#     right_curr = right_head

#     curr = head
#     while curr is not None:
#         count_dict['comparisons'] += 1
#         if curr.data < pivot:
#             left_curr.next = curr
#             left_curr = curr
#         else:
#             right_curr.next = curr
#             right_curr = curr
#         curr = curr.next
#         count_dict['exchanges'] += 1

#     left_curr.next = None
#     right_curr.next = None

#     return left_head.next, right_head.next

# def partition_size(head):
#     size = 0
#     curr = head
#     while curr is not None:
#         size += 1
#         curr = curr.next
#     return size

# def insertion_sort(head, count_dict):
#     if head is None or head.next is None:
#         return head

#     sorted_head = head
#     head = head.next
#     sorted_head.next = None

#     while head is not None:
#         curr = head
#         head = head.next

#         count_dict['comparisons'] += 1
#         if curr.data < sorted_head.data:
#             curr.next = sorted_head
#             sorted_head = curr
#         else:
#             prev = sorted_head
#             while prev.next is not None and prev.next.data < curr.data:
#                 count_dict['comparisons'] += 1
#                 prev = prev.next
#             curr.next = prev.next
#             prev.next = curr

#         count_dict['exchanges'] += 1

#     return sorted_head

# def quick_sort(head, count_dict):
#     if head is None or head.next is None:
#         return head

#     pivot = head.data
#     left_head, right_head = partition(head.next, pivot, count_dict)

#     left_sorted = quick_sort(left_head, count_dict)
#     right_sorted = quick_sort(right_head, count_dict)

#     return merge(left_sorted, right_sorted, pivot, count_dict)

# def quick_sort_insertion_50(head, count_dict):
#     if head is None or head.next is None:
#         return head

#     stack = []
#     stack.append((head, None))

#     new_head = None
#     new_tail = None

#     while stack:
#         low, high = stack.pop()

#         if low is None or low.next is None:
#             if new_head is None:
#                 new_head = low
#                 new_tail = high
#             else:
#                 new_tail.next = low
#                 if high is not None:
#                     new_tail = high
#             continue

#         pivot = low.data
#         left_head, right_head = partition(low.next, pivot, count_dict)

#         if partition_size(left_head) <= 50:
#             left_sorted = insertion_sort(left_head, count_dict)
#         else:
#             stack.append((left_head, None))
#             continue

#         if partition_size(right_head) <= 50:
#             right_sorted = insertion_sort(right_head, count_dict)
#         else:
#             stack.append((right_head, None))
#             continue

#         merged = merge(left_sorted, right_sorted, pivot, count_dict)
#         if new_head is None:
#             new_head = merged
#             while merged.next is not None:
#                 merged = merged.next
#             new_tail = merged
#         else:
#             new_tail.next = merged
#             while merged.next is not None:
#                 merged = merged.next
#             new_tail = merged

#     return new_head


# def merge(left, right, pivot, count_dict):
#     # Merge the two sublists and insert the pivot in its correct position
#     head = LinkedListNode(None)
#     curr = head
#     while left is not None and left.data < pivot:
#         count_dict['comparisons'] += 1
#         curr.next = left
#         curr = left
#         left = left.next
#         count_dict['exchanges'] += 1
#     curr.next = LinkedListNode(pivot)
#     curr = curr.next
#     count_dict['exchanges'] += 1
#     while left is not None:
#         curr.next = left
#         curr = left
#         left = left.next
#         count_dict['exchanges'] += 1
#     while right is not None:
#         curr.next = right
#         curr = right
#         right = right.next
#         count_dict['exchanges'] += 1
#     return head.next

# def sort_file(file_name):
#     with open(file_name, 'r') as f:
#         lines = f.readlines()
#         data = None
#         for line in lines:
#             for num in line.strip().split():
#                 if data is None:
#                     data = LinkedListNode(int(num))
#                     curr = data
#                 else:
#                     curr.next = LinkedListNode(int(num))
#                     curr = curr.next

#     print(f"File: {file_name}")
#     print("Data:", data)

#     count_dict = {'exchanges': 0, 'comparisons': 0}
#     sorted_data = quick_sort_insertion_50(data, count_dict)
#     return sorted_data, count_dict


# def main():
#     input_folder = './bigInput'
#     input_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.dat')]

#     output_dir = './quickSort50_output'
#     os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

#     for input_file in input_files:
#         sorted_data, count_dict = sort_file(input_file)
#         output_file = os.path.join(output_dir, 'Output' + os.path.basename(input_file))

#         with open(output_file, 'w') as f:
#             curr = sorted_data
#             while curr is not None:
#                 f.write(str(curr.data) + '\n')
#                 curr = curr.next

#         print(f'Sorted list for file {os.path.basename(input_file)}:')
#         curr = sorted_data
#         while curr is not None:
#             print(curr.data)
#             curr = curr.next

#         print(f"Exchanges: {count_dict['exchanges']}, Comparisons: {count_dict['comparisons']}")

# if __name__ == '__main__':
#     main()

import os
import glob

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def partition(head, pivot, count_dict):
    left_head = LinkedListNode(None)
    right_head = LinkedListNode(None)
    left_curr = left_head
    right_curr = right_head

    curr = head
    while curr is not None:
        count_dict['comparisons'] += 1
        if curr.data < pivot:
            left_curr.next = curr
            left_curr = curr
        else:
            right_curr.next = curr
            right_curr = curr
        curr = curr.next
        count_dict['exchanges'] += 1

    left_curr.next = None
    right_curr.next = None

    return left_head.next, right_head.next

def partition_size(head):
    size = 0
    curr = head
    while curr is not None:
        size += 1
        curr = curr.next
    return size

def insertion_sort(head, count_dict):
    if head is None or head.next is None:
        return head

    sorted_head = head
    head = head.next
    sorted_head.next = None

    while head is not None:
        curr = head
        head = head.next

        count_dict['comparisons'] += 1
        if curr.data < sorted_head.data:
            curr.next = sorted_head
            sorted_head = curr
        else:
            prev = sorted_head
            while prev.next is not None and prev.next.data < curr.data:
                count_dict['comparisons'] += 1
                prev = prev.next
            curr.next = prev.next
            prev.next = curr

        count_dict['exchanges'] += 1

    return sorted_head

def quick_sort_insertion_50(head, count_dict):
    if head is None or head.next is None:
        return head

    stack = []
    stack.append((head, None))

    new_head = None
    new_tail = None

    while stack:
        low, high = stack.pop()

        if low is None or low.next is None:
            if new_head is None:
                new_head = low
                new_tail = high
            else:
                new_tail.next = low
                if high is not None:
                    new_tail = high
            continue

        pivot = low.data
        left_head, right_head = partition(low.next, pivot, count_dict)

        if partition_size(left_head) < 50:
            left_sorted = insertion_sort(left_head, count_dict)
        else:
            stack.append((left_head, None))
            continue

        if partition_size(right_head) < 50:
            right_sorted = insertion_sort(right_head, count_dict)
        else:
            stack.append((right_head, None))
            continue

        merged = merge(left_sorted, right_sorted, pivot, count_dict)
        if new_head is None:
            new_head = merged
            while merged.next is not None:
                merged = merged.next
            new_tail = merged
        else:
            new_tail.next = merged
            while merged.next is not None:
                merged = merged.next
            new_tail = merged

    return new_head


def merge(left, right, pivot, count_dict):
    head = LinkedListNode(None)
    curr = head
    while left is not None and left.data < pivot:
        count_dict['comparisons'] += 1
        curr.next = left
        curr = left
        left = left.next
    count_dict['exchanges'] += 1
    curr.next = LinkedListNode(pivot)
    curr = curr.next
    count_dict['exchanges'] += 1
    while left is not None:
        curr.next = left
        curr = left
        left = left.next
        count_dict['exchanges'] += 1
    while right is not None:
        curr.next = right
        curr = right
        right = right.next
        count_dict['exchanges'] += 1
    return head.next

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

    print(f"File: {file_name}")
    print("Data:", data)

    count_dict = {'exchanges': 0, 'comparisons': 0}
    sorted_data = quick_sort_insertion_50(data, count_dict)
    return sorted_data, count_dict


def main():
    input_folder = './bigInput'
    input_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.dat')]

    output_dir = './quickSort50_output'
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

    for input_file in input_files:
        sorted_data, count_dict = sort_file(input_file)
        output_file = os.path.join(output_dir, 'Output' + os.path.basename(input_file))

        with open(output_file, 'w') as f:
            curr = sorted_data
            while curr is not None:
                f.write(str(curr.data) + '\n')
                curr = curr.next

            # Add exchanges and comparisons at the end of the output file
            f.write(f"Exchanges: {count_dict['exchanges']}, Comparisons: {count_dict['comparisons']}")

        print(f'Sorted list for file {os.path.basename(input_file)}:')
        curr = sorted_data
        while curr is not None:
            print(curr.data)
            curr = curr.next

        print(f"Exchanges: {count_dict['exchanges']}, Comparisons: {count_dict['comparisons']}")

if __name__ == '__main__':
    main()

