# # First we must convert prefix to infix. As we learned in class, the steps to this are reading from right to left (except for the case of exponent), if the value is an operand then pop it to the stack, if it is an operator we pop off 2 operands from the stack, append the operator to the first operand, then the second operand to them. We then push this back to the stack and repeat

# import sys

# def preToPostfix(prefix_expression):
#     operators = set(['+', '-', '*', '/', '$'])
#     operands = []

#     # Iterate through the expression from right to left
#     for i in range(len(prefix_expression) - 1, -1, -1):
#         current = prefix_expression[i]

#         # If the current character isnt an operator, letter, or number, return error
#         if current not in operators and not current.isalpha() and not current.isdigit():
#             return "Error: equation contains invalid characters"
        
#         # If the current character is an operand, add it to the postfix expression
#         if current not in operators:
#             operands.append(current)
#         # If the current character is an operator, pop two operands from the operands and
#         # add them to the postfix expression along with the operator
#         else:
#             try:
#                 operand_1 = operands.pop()
#                 operand_2 = operands.pop()
#                 operands.append(operand_1 + operand_2 + current)
#             except IndexError:
#                 # If there is an error, continue to the next line of equation
#                 return "Error: equation not formatted properly"

#     # Return the final postfix expression
#     return ''.join(operands)

# # if __name__ == "__main__":
# #     prefix_expression = sys.argv[1]
# #     postfix_expression = preToPostfix(prefix_expression)
# #     print(postfix_expression)

# if __name__ == "__main__":
#     # Get the input and output file names from the command-line arguments
#     input_file = sys.argv[1]
#     output_file = sys.argv[2]

#     # Open the input file for reading
#     with open(input_file, "r") as file:
#         # Read the prefix expression from the input file
#         prefix_expression = file.read().strip()

#     # Convert the prefix expression to postfix
#     postfix_expression = preToPostfix(prefix_expression)

#     # Open the output file for writing
#     with open(input_file, "r") as input_file_obj, open(output_file, "w") as output_file_obj:
#         # Read each line from the input file
#         for line in input_file_obj:
#             # Strip whitespace from the line
#             line = line.strip()

#             # Skip empty lines
#             if not line:
#                 continue

#             # Convert the prefix expression to postfix
#             postfix_expression = preToPostfix(line)

#             # Write the postfix expression to the output file as prefix_expression = postfix_expression
#             # output_file_obj.write(postfix_expression + '\n')
#             output_file_obj.write('The output of ' + line + ' = ' + postfix_expression + '\n' + '\n')
