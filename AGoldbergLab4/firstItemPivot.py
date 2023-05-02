import os
import glob

#define a class for LinkedListNode
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

#function to perform iterative quick sort on a linked list
def quick_sort_iterative(head):
    if head is None or head.next is None:
        return head, 0, 0

    compare_counter = 0
    exchange_counter = 0
    stack = [(head, None)]

    # main loop for the iterative quick sort
    while stack:
        start, end = stack.pop()

        if start is None or start == end:
            continue

        pivot = start.data
        left_head = LinkedListNode(None)
        left_tail = left_head
        right_head = LinkedListNode(None)
        right_tail = right_head
        curr = start.next
        prev = start

        # Partition the list into left and right sublists
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

        start.data = left_tail.data
        left_tail.data = pivot

        # Add the sublists back to the stack
        stack.append((left_head.next, left_tail))
        stack.append((left_tail.next, end))

    return head, compare_counter, exchange_counter

#Function to sort a file using iterative quick sort
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

# Main function to process input files and output sorted files
def main():
    input_dirs = ['./50input', './bigInput']
    output_dir = './FirstItemPivotOutput'
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate through input files, sort them, and write the results to output files
    for input_dir in input_dirs:
        input_files = glob.glob(input_dir + '/*.dat')
        for input_file in input_files:
            sorted_data, compare_counter, exchange_counter = sort_file(input_file)
            output_file = os.path.join(output_dir, 'Output' + os.path.basename(input_file))
            with open(output_file, 'w') as f:
                curr = sorted_data
                while curr is not None:
                    f.write(str(curr.data) + '\n')
                    curr = curr.next
                f.write(f'Comparisons: {compare_counter}, Exchanges: {exchange_counter}\n')

if __name__ == '__main__':
    main()
