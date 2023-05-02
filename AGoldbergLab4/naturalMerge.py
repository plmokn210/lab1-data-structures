import os
import glob

#define a class for LinkedListNode
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

#function to perform merge sort on a linked list with a provided count_dict for comparisons and exchanges
def merge_sort_linked_list(head, count_dict):
    if not head or not head.next:
        return head
    left_half, right_half = split_linked_list(head)
    left_half = merge_sort_linked_list(left_half, count_dict)
    right_half = merge_sort_linked_list(right_half, count_dict)
    return merge_linked_lists(left_half, right_half, count_dict)

# Function to split a linked list into two halves
def split_linked_list(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    right_half = slow.next
    slow.next = None
    return head, right_half

#Function to merge two sorted linked lists
def merge_linked_lists(left, right, count_dict):
    dummy = LinkedListNode(None)
    curr = dummy
    while left and right:
        count_dict['comparisons'] += 1
        if left.data <= right.data:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
        count_dict['exchanges'] += 1
    if left:
        curr.next = left
    else:
        curr.next = right
    return dummy.next

# Function to sort a file using merge sort
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
        sorted_data = merge_sort_linked_list(data, count_dict)
        return sorted_data, count_dict

#main function to process input files and output sorted files
def main():
    input_dirs = ['./50input', './bigInput']
    output_dir = './MergeSortOutput'
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through input files, sort them, and write the results to output files
    for input_dir in input_dirs:
        input_files = glob.glob(input_dir + '/*.dat')
        for input_file in input_files:
            sorted_data, count_dict = sort_file(input_file)
            output_file = os.path.join(output_dir, 'Output' + os.path.basename(input_file))
            with open(output_file, 'w') as f:
                if input_dir == './50input':
                    curr = sorted_data
                    while curr is not None:
                        f.write(str(curr.data) + '\n')
                        curr = curr.next
                f.write(f"Comparisons: {count_dict['comparisons']}, Exchanges: {count_dict['exchanges']}\n")

if __name__ == '__main__':
    main()
