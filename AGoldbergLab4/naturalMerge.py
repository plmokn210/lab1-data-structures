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

def merge_sort_linked_list(head, count_dict):
    if not head or not head.next:
        return head
    left_half, right_half = split_linked_list(head)
    left_half = merge_sort_linked_list(left_half, count_dict)
    right_half = merge_sort_linked_list(right_half, count_dict)
    return merge_linked_lists(left_half, right_half, count_dict)

def split_linked_list(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    right_half = slow.next
    slow.next = None
    return head, right_half

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

def main():
    input_dirs = ['./50input', './bigInput']
    output_dir = './MergeSortOutput'
    os.makedirs(output_dir, exist_ok=True)
    
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
