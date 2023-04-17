# #import counter from counter.py
# from counter import Counter
# from heap import heappush, heappop

# class Node:
#     def __init__(self, freq, char='', left=None, right=None):
#         self.freq = freq
#         self.char = char
#         self.left = left
#         self.right = right

#     def __lt__(self, other):
#         if self.freq == other.freq:
#             if len(self.char) == 1 and len(other.char) > 1:
#                 return True
#             elif len(self.char) > 1 and len(other.char) == 1:
#                 return False
#             else:
#                 return self.char.lower() < other.char.lower()
#         return self.freq < other.freq


# def build_tree(text):
#     freqs = Counter(text)
#     heap = [Node(freq, char) for char, freq in freqs.items()]
#     while len(heap) > 1:
#         left = heappop(heap)
#         right = heappop(heap)
#         heappush(heap, Node(left.freq + right.freq, left=left, right=right))
#     return heap[0]


# def build_code(node, code=''):
#     if node.char:
#         return {node.char: code}
#     else:
#         code_dict = {}
#         code_dict.update(build_code(node.left, code + '0'))
#         code_dict.update(build_code(node.right, code + '1'))
#         return code_dict


# def write_tree(node, file, indent=''):
#     if node.char:
#         file.write(f"{indent}+-- '{node.char}':{node.freq}\n")
#     else:
#         file.write(f"{indent}+-- {node.freq}\n")
#         write_tree(node.left, file, indent + '|   ')
#         write_tree(node.right, file, indent + '    ')


# def encode_text(text, code_dict):
#     encoded = ''
#     for char in text:
#         if char.isalpha():
#             encoded += code_dict[char.lower()]
#     return encoded


# def decode_text(encoded, code_dict):
#     decoded = ''
#     code = ''
#     for bit in encoded:
#         code += bit
#         if code in code_dict:
#             decoded += code_dict[code]
#             code = ''
#     return decoded


# if __name__ == '__main__':
#     with open('ClearText.txt', 'r') as f:
#         text = f.read().strip()
#     root = build_tree(text)
#     code_dict = build_code(root)

#     try:
#         with open('encodedstuff.txt', 'r') as f:
#             encoded = f.read().strip()
#     except FileNotFoundError:
#         encoded = encode_text(text, code_dict)

#     decoded = decode_text(encoded, {v: k for k, v in code_dict.items()})
#     with open('tree.txt', 'w') as f:
#         write_tree(root, f)
#     with open('encodedstuff.txt', 'w') as f:
#         f.write(encoded)
#     with open('decoded.txt', 'w') as f:
#         f.write(decoded)

# Import the Counter class from the counter.py file
from counter import Counter

# Define a node class for building the Huffman tree
class Node:
    def __init__(self, freq, char='', left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    # Define the less-than operator for sorting nodes by frequency
    def __lt__(self, other):
        if self.freq == other.freq:
            # If two nodes have the same frequency, sort them by character count (lower count first)
            if len(self.char) == 1 and len(other.char) > 1:
                return True
            elif len(self.char) > 1 and len(other.char) == 1:
                return False
            else:
                # If both nodes have the same character count, sort them alphabetically (lower character first)
                return self.char.lower() < other.char.lower()
        # Otherwise, sort them by frequency (lower frequency first)
        return self.freq < other.freq


# Define a function for building the Huffman tree
def build_tree(text):
    # Count the frequency of each character in the text using the Counter class
    freqs = Counter(text)

    # Convert each character frequency pair into a leaf node, and add them to a list (the initial "heap")
    heap = [Node(freq, char) for char, freq in freqs.items()]

    # Repeatedly combine the two lowest frequency nodes into a new parent node, until only one node remains (the root)
    while len(heap) > 1:
        # Get the two lowest frequency nodes (using heappop, which is not used in this version)
        left = heap[0]
        right = heap[1]

        # Remove the two lowest frequency nodes from the heap
        heap = heap[2:]

        # Create a new parent node with the sum of the frequencies of its children
        parent = Node(left.freq + right.freq, left=left, right=right)

        # Add the new parent node to the heap (not using heappush in this version)
        heap.append(parent)

        # Sort the heap by frequency, using the less-than operator defined in the Node class
        heap.sort()

    # Return the root node of the Huffman tree
    return heap[0]


# Define a function for building the code dictionary (mapping each character to its binary code)
def build_code(node, code=''):
    # If the current node is a leaf node, add its character and code to the dictionary
    if node.char:
        return {node.char: code}
    # Otherwise, recursively build the code for the left and right children and combine them
    else:
        code_dict = {}
        code_dict.update(build_code(node.left, code + '0'))
        code_dict.update(build_code(node.right, code + '1'))
        return code_dict


# Define a function for writing the Huffman tree to a file in ASCII art format
def write_tree(node, file, indent=''):
    # If the current node is a leaf node, write its character and frequency to the file
    if node.char:
        file.write(f"{indent}+-- '{node.char}':{node.freq}\n")
    # Otherwise, write its frequency and recurse on the left and right children (with incremented indentation)
    else:
        file.write(f"{indent}+-- {node.freq}\n")
        write_tree(node.left, file, indent + '|   ')
        write_tree(node.right, file, indent + '    ')


def encode_text(text, code_dict):
    # Initialize an empty string for the encoded text
    encoded = ''
    # Loop through each character in the input text
    for char in text:
        # If the character is a letter (i.e., in the code_dict), append the corresponding code to the encoded string
        if char.isalpha():
            encoded += code_dict[char.lower()]
    # Return the encoded string
    return encoded


def decode_text(encoded, code_dict):
    # Initialize an empty string for the decoded text and an empty string for the current code
    decoded = ''
    code = ''
    # Loop through each bit in the encoded string
    for bit in encoded:
        # Append the current bit to the current code
        code += bit
        # If the current code is in the code_dict (i.e., corresponds to a character), append the corresponding character to the decoded string and reset the current code
        if code in code_dict:
            decoded += code_dict[code]
            code = ''
    # Return the decoded string
    return decoded


if __name__ == '__main__':
    # Read in the input text from a file and remove any leading or trailing whitespace
    with open('ClearText.txt', 'r') as f:
        text = f.read().strip()
    # Build the Huffman tree from the input text
    root = build_tree(text)
    # Build the code dictionary from the Huffman tree
    code_dict = build_code(root)

    try:
        # Try to read in the encoded text from a file (if it exists)
        with open('encodedstuff.txt', 'r') as f:
            encoded = f.read().strip()
    except FileNotFoundError:
        # If the encoded text file doesn't exist, encode the input text and save the result to the file
        encoded = encode_text(text, code_dict)
    # Decode the encoded text using the code dictionary and save the result to a file
    decoded = decode_text(encoded, {v: k for k, v in code_dict.items()})
    with open('tree.txt', 'w') as f:
        # Write the Huffman tree to a file using a recursive function
        write_tree(root, f)
    with open('encodedstuff.txt', 'w') as f:
        # Write the encoded text to a file
        f.write(encoded)
    with open('decoded.txt', 'w') as f:
        # Write the decoded text to a file
        f.write(decoded)
