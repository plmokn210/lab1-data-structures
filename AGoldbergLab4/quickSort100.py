import os
import glob

#define a linked list node class
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

#quick sort function for a linked list (iterative version)
def quick_sort_iterative(head):
    if head is None or head.next is None:
        return head, 0, 0

    compare_counter = 0
    exchange_counter = 0
    stack = [(head, None)]

    #Continue sorting while there are still unprocessed segments
    while stack:
        start, end = stack.pop()

        if start is None or start == end:
            continue

        # Choose pivot and initialize left and right partitions
        pivot = start.data
        left_head = LinkedListNode(None)
        left_tail = left_head
        right_head = LinkedListNode(None)
        right_tail = right_head
        curr = start.next
        prev = start

        # Partition the linked list based on the pivot
        while curr != end:
            compare_counter += 1
            if curr.data < pivot:
                exchange_counter += 1
                left_tail.next = curr
                left_tail = curr
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        left_tail.next = None
        right_tail.next = None

        # Swap pivot with the last element of the left partition
        start.data = left_tail.data
        left_tail.data = pivot

        # Process left and right partitions
        left_sorted = left_head.next
        if left_tail is not None and partition_size(left_sorted, left_tail) <= 100:
            left_sorted = insertion_sort(left_sorted)
            left_tail = get_tail(left_sorted)
        else:
            stack.append((left_sorted, left_tail))

        if left_tail is not None:
            right_sorted = left_tail.next
            if partition_size(right_sorted, end) <= 100:
                right_sorted = insertion_sort(right_sorted)
            else:
                stack.append((right_sorted, end))

    return head, compare_counter, exchange_counter

# Calculate the size of the partition between the start and end nodes
def partition_size(start, end):
    size = 0
    curr = start
    while curr is not None and curr != end:
        size += 1
        curr = curr.next
    return size

#get tail node of a linked list
def get_tail(head):
    if head is None:
        return None
    while head.next is not None:
        head = head.next
    return head

#insertion sort function for a linked list
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

# Sort a file with the quick sort iterative algorithm
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
        sorted_data, compare_counter, exchange_counter = quick_sort_iterative(data)
        return (sorted_data, compare_counter, exchange_counter)

# Main function to process input files and sort them using the quick sort iterative algorithm
def main():
    input_dirs = ['./50input', './bigInput']
    output_dir = './quickSort100Output'
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each input file in the input directories
    for input_dir in input_dirs:
        input_files = glob.glob(input_dir + '/*.dat')
        for input_file in input_files:
            sorted_data, compare_counter, exchange_counter = sort_file(input_file)
            output_file = os.path.join(output_dir, 'Output' + os.path.basename(input_file))
            
            # Write the sorted data and statistics to the output file
            with open(output_file, 'w') as f:
                curr = sorted_data
                while curr is not None:
                    f.write(str(curr.data) + '\n')
                    curr = curr.next
                f.write(f'Comparisons: {compare_counter}, Exchanges: {exchange_counter}\n')

if __name__ == '__main__':
    main()
