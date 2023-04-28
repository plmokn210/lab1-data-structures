import os
import glob

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def quick_sort(head):
    if head is None or head.next is None:
        return head

    # Partition the list into two sublists around the pivot
    pivot = head.data
    left_head = LinkedListNode(None)
    left_tail = left_head
    right_head = LinkedListNode(None)
    right_tail = right_head
    curr = head.next
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

    # Sort the sublists recursively and merge them together
    left_sorted = quick_sort(left_head.next)
    right_sorted = quick_sort(right_head.next)
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
    output_dir = './FirstItemPivotOutput'
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
