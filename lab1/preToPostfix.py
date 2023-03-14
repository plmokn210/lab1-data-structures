# # This is the actual program that will run. It takes the prefix expression from the input file and converts it to postfix
# def preToPostfix(prefix_expression):
#     operators = set(['+', '-', '*', '/', '$'])
#     operands = []

#     # Iterate through the expression from right to left
#     for i in range(len(prefix_expression) - 1, -1, -1):
#         current = prefix_expression[i]

#         # If there is input that isnt a valid character, return an error
#         if current not in operators and not current.isalpha() and not current.isdigit():
#             return "Error: equation contains invalid characters"
        
#         # If the current character is an operand, add it to the operands stack
#         if current not in operators:
#             operands.append(current)
#         # If the current character is an operator, pop two operands from the stack and
#         # add them to the postfix expression along with the operator
#         else:
#             try:
#                 operand_1 = operands.pop()
#                 operand_2 = operands.pop()
#                 operands.append(operand_1 + operand_2 + current)
#             except IndexError:
#                 return "Error: equation not formatted properly"

#     # Return the postfix expression and the value of the expression if it consists of digits
#     return ''.join(operands)

# This function takes a prefix expression as input and converts it to postfix notation.
# Prefix notation is where the operator comes before the operands (e.g. +AB)
# Postfix notation is where the operator comes after the operands (e.g. AB+)

def preToPostfix(input):
    # Define a set of operators to be used in the prefix expression
    operators = set(['+', '-', '*', '/', '$'])
    # If input is empty, return None instead of an empty string
    if not input:
        return None  
    # Get the first character of the input
    char = input[0]
    # If the first character is an operator, recursively call preToPostfix on the rest of the input
    if char in operators:
        # Get the left and right expressions by recursively calling preToPostfix on the input
        # Note that the left expression is the rest of the input after the first character, 
        # and the right expression is the rest of the input after the left expression
        left = preToPostfix(input[1:])
        right = preToPostfix(input[len(preToPostfix(input[1:]))+1:])
        # Check if either the left or right expression is None before concatenating them
        if left is None or right is None:
            # Return an empty string if either the left or right expression is None
            return "Error: equation not formatted properly"
        # Concatenate the left and right expressions, followed by the operator character
        return left + right + char
    else:
        # If the first character is not an operator, digit, or letter, return an error
        if not char.isdigit() and not char.isalpha():
            return "Error: equation contains invalid characters"
        # If the first character is not an operator, return it
        return char

        
