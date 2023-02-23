import sys
from preToPostfix import preToPostfix

if __name__ == "__main__":
    # Get the input and output file names from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Open the input file for reading
    with open(input_file, "r") as file:
        # Read the prefix expression from the input file
        prefix_expression = file.read().strip()

    # Convert the prefix expression to postfix
    postfix_expression = preToPostfix(prefix_expression)

    # Open the output file for writing
    with open(input_file, "r") as input_file_obj, open(output_file, "w") as output_file_obj:
        # Read each line from the input file
        for line in input_file_obj:
            # Strip whitespace from the line
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Convert the prefix expression to postfix
            postfix_expression = preToPostfix(line)

            # Write the postfix expression to the output file as prefix_expression = postfix_expression
            output_file_obj.write('The output of ' + line + ' = ' + postfix_expression + '\n' + '\n')
