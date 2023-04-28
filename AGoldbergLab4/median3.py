import os
import glob
from typing import List, Tuple, Callable


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def partition(node, pivot):
    left_head = LinkedListNode(None)
    left_tail = left_head
    right_head = LinkedListNode(None)
    right_tail = right_head
    curr = node
    while curr is not None:
        if curr.data < pivot:
            left_tail.next = curr
            left_tail = curr
        else:
            right_tail.next = curr
            right_tail = curr
        curr = curr.next
    left_tail.next = None
    right_tail.next = None
    return left_head.next, right_head.next


def partition_size(node):
    count = 0
    curr = node
    while curr is not None:
        count += 1
        curr = curr.next
    return count


def insertion_sort(head):
    if head is None:
        return head

    sorted_head = LinkedListNode(None)
    curr = head

    while curr is not None:
        next_node = curr.next
        curr.next = None
        sorted_head = insert(sorted_head, curr)
        curr = next_node

    return sorted_head.next


def insert(sorted_head, node):
    prev = sorted_head
    curr = sorted_head.next

    while curr is not None and curr.data < node.data:
        prev = curr
        curr = curr.next

    prev.next = node
    node.next = curr
    return sorted_head


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


def merge(left, right, pivot):
    # Merge the two sublists and insert the pivot in its correct position
    head = LinkedListNode(None)
    curr = head
    while left is not None and left.data < pivot:
        curr.next = left
        curr = left
        left = left.next
    curr.next = LinkedListNode(pivot)
    curr = curr.next
    while left is not None:
        curr.next = left
        curr = left
        left = left.next
    while right is not None:
        curr.next = right
        curr = right
        right = right.next
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

        # Convert linked list to list
        arr = []
        curr = data
        while curr is not None:
            arr.append(curr.data)
            curr = curr.next

        # Perform insertion sort on partitions of size 10
        partition_size = 10
        curr = data
        sorted_data = None
        sorted_tail = None

        while curr is not None:
            # Partition the list into a sublist of size 10
            sublist_head = curr
            sublist_tail = curr
            for i in range(partition_size - 1):
                if sublist_tail.next is not None:
                    sublist_tail = sublist_tail.next

            # Save the next node after the sublist
            next_node = sublist_tail.next
            sublist_tail.next = None

            # Sort the sublist using insertion sort
            sorted_sublist = insertion_sort(sublist_head)

            # Append the sorted sublist to the sorted list
            if sorted_data is None:
                sorted_data = sorted_sublist
                sorted_tail = sorted_sublist
            else:
                sorted_tail.next = sorted_sublist
                while sorted_tail.next is not None:
                    sorted_tail = sorted_tail.next

            # Move to the next partition
            curr = next_node

        # Perform quicksort on the final sorted list
        quicksort_median(arr, 0, len(arr)-1)

        # Create a new linked list from the sorted list
        sorted_data = LinkedListNode(arr[0])
        curr = sorted_data
        for i in range(1, len(arr)):
            curr.next = LinkedListNode(arr[i])
            curr = curr.next

        return sorted_data




def main():
    input_files = glob.glob('./50input/*.dat')
    output_dir = './median3Output'
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
#print hello world
    print('hello 1')
    for input_file in input_files:
        sorted_data = sort_file(input_file)
        print('hello 2')
        output_file = os.path.join(output_dir, 'Output' + os.path.basename(input_file))
        with open(output_file, 'w') as f:
            curr = sorted_data
            while curr is not None:
                f.write(str(curr.data) + '\n')
                curr = curr.next
        print(f'Sorted list for file {os.path.basename(input_file)}:')
        curr = sorted_data
        while curr is not None:
            print(curr.data)
            curr = curr.next
        print(sorted_data)


if __name__ == '__main__':
    main()
