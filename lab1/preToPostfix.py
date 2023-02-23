# This is the actual program that will run. It takes the prefix expression from the input file and converts it to postfix
def preToPostfix(prefix_expression):
    operators = set(['+', '-', '*', '/', '$'])
    operands = []

    # Iterate through the expression from right to left
    for i in range(len(prefix_expression) - 1, -1, -1):
        current = prefix_expression[i]

        # If there is input that isnt a valid character, return an error
        if current not in operators and not current.isalpha() and not current.isdigit():
            return "Error: equation contains invalid characters"
        
        # If the current character is an operand, add it to the operands stack
        if current not in operators:
            operands.append(current)
        # If the current character is an operator, pop two operands from the stack and
        # add them to the postfix expression along with the operator
        else:
            try:
                operand_1 = operands.pop()
                operand_2 = operands.pop()
                operands.append(operand_1 + operand_2 + current)
            except IndexError:
                return "Error: equation not formatted properly"

    # Return the postfix expression
    return ''.join(operands)
