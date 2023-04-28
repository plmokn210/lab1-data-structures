import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def merge(first, second):
    if not first:
        return second
    if not second:
        return first
    
    if first.data < second.data:
        result = first
        result.next = merge(first.next, second)
    else:
        result = second
        result.next = merge(first, second.next)
        
    return result

def split(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    mid = slow.next
    slow.next = None
    
    return head, mid

def natural_merge_sort(head):
    # Initialize variables
    if not head or not head.next:
        return head
    run_head = head
    tail = Node(None)
    while True:
        count = 0
        right_head = run_head
        # Find the end of the first run
        while right_head.next and right_head.data <= right_head.next.data:
            right_head = right_head.next
        # If we've reached the end of the list, we're done
        if not right_head.next:
            if count == 0:
                return head
            tail.next = head
            head = run_head
            continue
        left_head = right_head.next
        # Find the end of the second run
        while left_head.next and left_head.data <= left_head.next.data:
            left_head = left_head.next
        # Merge the two runs
        merge(head, run_head, right_head, left_head, tail)
        # Move the head pointer to the next run
        head = run_head
        # Count the number of runs merged
        count += 1


def read_input_file(filename):
    head = None
    with open(filename, 'r') as f:
        for line in f:
            line_numbers = line.strip().split()
            for number in line_numbers:
                data = int(number)
                new_node = Node(data)
                if not head:
                    head = new_node
                else:
                    current = head
                    while current.next:
                        current = current.next
                    current.next = new_node
    return head


def print_list(head):
    current = head
    while current:
        print(current.data)
        current = current.next

directory = '50input'
for filename in os.listdir(directory):
    if filename.endswith('.dat'):
        input_file = os.path.join(directory, filename)
        data = read_input_file(input_file)
        sorted_data = natural_merge_sort(data)
        print("Sorted list for file {}:".format(filename))
        print_list(sorted_data)
