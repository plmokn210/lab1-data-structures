# class Node:
#     def __init__(self, data=None, next_node=None):
#         self.data = data
#         self.next = next_node

# def merge_sort_linked_list(head):
#     if not head or not head.next:
#         return head
#     left_half, right_half = split_linked_list(head)
#     left_half = merge_sort_linked_list(left_half)
#     right_half = merge_sort_linked_list(right_half)
#     return merge_linked_lists(left_half, right_half)

# def split_linked_list(head):
#     slow = head
#     fast = head.next
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     right_half = slow.next
#     slow.next = None
#     return head, right_half

# def merge_linked_lists(left, right):
#     dummy = Node()
#     curr = dummy
#     while left and right:
#         if left.data <= right.data:
#             curr.next = left
#             left = left.next
#         else:
#             curr.next = right
#             right = right.next
#         curr = curr.next
#     if left:
#         curr.next = left
#     else:
#         curr.next = right
#     return dummy.next

# def natural_merge_sort(head):
#     if not head or not head.next:
#         return head
#     is_sorted = False
#     while not is_sorted:
#         is_sorted = True
#         current = head
#         prev = None
#         while current:
#             first = current
#             second = current.next
#             if second and second.data < first.data:
#                 is_sorted = False
#                 while second and second.data < first.data:
#                     first = second
#                     second = second.next
#                 if not prev:
#                     head = merge_linked_lists(current, first)
#                 else:
#                     prev.next = merge_linked_lists(current, first)
#                 current = prev.next
#             else:
#                 prev = current
#                 current = current.next
#     return head

# # Example usage
# arr = [7, 2, 1, 6, 8, 5, 3, 4]
# head = Node(arr[0])
# current = head
# for i in range(1, len(arr)):
#     node = Node(arr[i])
#     current.next = node
#     current = current.next

# sorted_list = natural_merge_sort(head)
# while sorted_list:
#     print(sorted_list.data, end=" ")
#     sorted_list = sorted_list.next

import os
import glob

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def natural_merge_sort(head):
    if head is None or head.next is None:
        return head
    
    # Find all sorted runs in the list
    runs = []
    curr = head
    while curr is not None:
        run_head = curr
        while curr.next is not None and curr.data <= curr.next.data:
            curr = curr.next
        runs.append(run_head)
        curr = curr.next
        
    # Merge all the sorted runs together
    while len(runs) > 1:
        merged_runs = []
        for i in range(0, len(runs), 2):
            if i+1 < len(runs):
                merged = merge(runs[i], runs[i+1])
            else:
                merged = runs[i]
            merged_runs.append(merged)
        runs = merged_runs
        
    return runs[0]

def merge(left, right):
    # Merge two sorted linked lists together
    head = LinkedListNode(None)
    curr = head
    while left is not None and right is not None:
        if left.data <= right.data:
            curr.next = left
            curr = left
            left = left.next
        else:
            curr.next = right
            curr = right
            right = right.next
    if left is not None:
        curr.next = left
    else:
        curr.next = right
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
        sorted_data = natural_merge_sort(data)
        return sorted_data

def main():
    input_files = glob.glob('./50input/*.dat')
    output_dir = './NaturalMergeSortOutput'
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
