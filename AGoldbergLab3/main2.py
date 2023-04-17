import heapq

class HuffmanNode:
    def __init__(self, frequency, char=None, left=None, right=None):
        # constructor to initialize the attributes of HuffmanNode
        self.frequency = frequency
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        # less than method used for priority queue
        return self.frequency < other.frequency

    def __str__(self):
        # string representation of HuffmanNode object
        if self.char is None:
            return f":{self.frequency}"
        else:
            return f"{self.char}:{self.frequency}"


def build_huffman_tree(frequencies):
    # function to build the Huffman tree using a priority queue
    heap = [HuffmanNode(freq, char) for char, freq in frequencies.items()]
    # create a list of HuffmanNodes using the frequency table
    heapq.heapify(heap)
    # convert the list into a priority queue
    while len(heap) > 1:
        # combine the two smallest elements in the queue
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(node1.frequency + node2.frequency, left=node1, right=node2)
        heapq.heappush(heap, merged)
    return heap[0]


def build_encoding_decoding_dicts(node):
    # function to build the encoding and decoding dictionaries
    encoding_dict = {}
    decoding_dict = {}

    def traverse(node, code):
        # helper function to traverse the Huffman tree and build the dictionaries
        if node.char is not None:
            encoding_dict[node.char] = code
            decoding_dict[code] = node.char
            return
        traverse(node.left, code + '0')
        traverse(node.right, code + '1')

    traverse(node, '')
    return encoding_dict, decoding_dict


def encode_string(s, encoding_dict):
    # function to encode a string using the encoding dictionary
    encoded = ''
    for char in s:
        if char in encoding_dict:
            encoded += encoding_dict[char]
        else:
            encoded += char
    return encoded


def decode_string(s, decoding_dict):
    # function to decode a string using the decoding dictionary
    code = ''
    decoded = ''
    for char in s:
        code += char
        if code in decoding_dict:
            decoded += decoding_dict[code]
            code = ''
    return decoded


def read_frequency_table(filename):
    # function to read the frequency table from a file
    with open(filename, 'r') as f:
        frequencies = {}
        for line in f:
            key, value = line.strip().split('-')
            frequencies[key] = int(value)
        return frequencies


def print_huffman_tree(node, file):
    # function to print the Huffman tree to a file
    def traverse(node, depth=0):
        if node is not None:
            file.write('{}{}:{}\n'.format('\t' * depth, node.char, node.frequency))
            traverse(node.left, depth+1)
            traverse(node.right, depth+1)

    traverse(node)


def main():
    freq_table = read_frequency_table('FreqTable.txt')
    huffman_tree = build_huffman_tree(freq_table)
    encoding_dict, decoding_dict = build_encoding_decoding_dicts(huffman_tree)

    with open('ClearText.txt', 'r') as f:
        text = f.read().strip()

    # encoded = encode_string(text, encoding_dict)
    # with open('EncodedText.txt', 'w') as f:
    #     f.write(encoded)

    # with open('EncodedText.txt', 'r') as f:
    #     encoded = f.read().strip()

    # decoded = decode_string(encoded, decoding_dict)
    # with open('DecodedText.txt', 'w') as f:
    #     f.write(decoded)

    with open('printedTree.txt', 'w') as f:
        print_huffman_tree(huffman_tree, f)


if __name__ == '__main__':
    main()