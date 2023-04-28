import os
import glob

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def partition(head, pivot):
    left_head = LinkedListNode(None)
    right_head = LinkedListNode(None)
    left_curr = left_head
    right_curr = right_head

    curr = head
    while curr is not None:
        if curr.data < pivot:
            left_curr.next = curr
            left_curr = curr
        else:
            right_curr.next = curr
            right_curr = curr
        curr = curr.next

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

def insertion_sort(head):
    if head is None or head.next is None:
        return head

    sorted_head = head
    head = head.next
    sorted_head.next = None

    while head is not None:
        curr = head
        head = head.next

        if curr.data < sorted_head.data:
            curr.next = sorted_head
            sorted_head = curr
        else:
            prev = sorted_head
            while prev.next is not None and prev.next.data < curr.data:
                prev = prev.next
            curr.next = prev.next
            prev.next = curr

    return sorted_head


def quick_sort(head):
    if head is None or head.next is None:
        return head

    pivot = head.data
    left_head, right_head = partition(head.next, pivot)

    left_sorted = quick_sort(left_head)
    right_sorted = quick_sort(right_head)

    return merge(left_sorted, right_sorted, pivot)

def quick_sort_insertion_50(head):
    if head is None or head.next is None:
        return head

    pivot = head.data
    left_head, right_head = partition(head.next, pivot)

    if partition_size(left_head) <= 50:
        left_sorted = insertion_sort(left_head)
    else:
        left_sorted = quick_sort_insertion_50(left_head)

    if partition_size(right_head) <= 50:
        right_sorted = insertion_sort(right_head)
    else:
        right_sorted = quick_sort_insertion_50(right_head)

    return merge(left_sorted, right_sorted, pivot)


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
        sorted_data = quick_sort(data)
        return sorted_data


def main():
    input_files = glob.glob('./50input/*.dat')
    output_dir = './quickSort50_output'
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
    for input_file in input_files:
        sorted_data = sort_file(input_file)
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
