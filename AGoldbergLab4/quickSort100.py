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

def quick_sort_insertion_100(head, count_dict):
    if head is None or head.next is None:
        return head

    stack = [(head, None)]
    sorted_head = LinkedListNode(None)
    sorted_tail = sorted_head

    while stack:
        node, end = stack.pop()

        if partition_size(node) <= 100:
            sorted_sublist = insertion_sort(node, count_dict)
            sorted_tail.next = sorted_sublist

            while sorted_tail.next is not None:
                sorted_tail = sorted_tail.next
        else:
            pivot = node.data
            left_head, right_head = partition(node.next, pivot, count_dict)

            sorted_tail.next = LinkedListNode(pivot)
            sorted_tail = sorted_tail.next

            if right_head is not None:
                stack.append((right_head, None))

            if left_head is not None:
                stack.append((left_head, None))

    return sorted_head.next


def merge(left, right, pivot, count_dict):
    head = LinkedListNode(None)
    curr = head
    while left is not None and left.data < pivot:
        count_dict['comparisons'] += 1
        curr.next = left
        curr = left
        left = left.next

    curr.next = LinkedListNode(pivot)
    curr = curr.next

    while left is not None:
        count_dict['comparisons'] += 1
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
        count_dict = {'comparisons': 0, 'exchanges': 0}
        sorted_data = quick_sort_insertion_100(data, count_dict)
        return sorted_data, count_dict

def main():
    input_files = glob.glob('./bigInput/*.dat')  # Update to read files from bigInput directory
    output_dir = './quickSort100Output'
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
    
    for input_file in input_files:
        sorted_data, count_dict = sort_file(input_file)
        output_file = os.path.join(output_dir, 'Output' + os.path.basename(input_file))
        
        with open(output_file, 'w') as f:
            curr = sorted_data
            while curr is not None:
                f.write(str(curr.data) + '\n')
                curr = curr.next
            f.write(f"Comparisons: {count_dict['comparisons']}\n")
            f.write(f"Exchanges: {count_dict['exchanges']}\n")
        
        print(f'Sorted list for file {os.path.basename(input_file)}:')
        curr = sorted_data
        while curr is not None:
            print(curr.data)
            curr = curr.next
        
        print(f"Exchanges: {count_dict['exchanges']}, Comparisons: {count_dict['comparisons']}")

if __name__ == '__main__':
    main()
