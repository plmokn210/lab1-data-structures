#This file reads the input file from the command line, runs the preToPostfix function on each line of the input file, and writes the output to the output file from the command line.

import sys # Import the sys module, this is used to get the command-line arguments
from preToPostfix import preToPostfix  # Import the preToPostfix function from the preToPostfix file

if __name__ == "__main__": 
    # Get the input and output file names from the command-line arguments. The first argument is the name of the input file, the second argument is the name of the output file
    input_file = sys.argv[1] 
    output_file = sys.argv[2] 

    # Open and read the input file
    with open(input_file, "r") as file:
        # Read the input file
        prefix_expression = file.read().strip()

    # Convert the prefix expressions to postfix by calling the preToPostfix function on the prefix expressions from the input file
    postfix_expression = preToPostfix(prefix_expression)

    # Open the output file for writing
    with open(input_file, "r") as input_file_obj, open(output_file, "w") as output_file_obj:
        # Read each line from the input file
        for line in input_file_obj:
            # Removes whitespace from the line
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Call the function on each line of the input file
            postfix_expression = preToPostfix(line)

            # Write the postfix expression to the output file as prefix_expression = postfix_expression and skip a line
            output_file_obj.write('The output of ' + line + ' = ' + postfix_expression + '\n' + '\n')
