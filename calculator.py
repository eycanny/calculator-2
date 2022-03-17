"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# repeat forever:
while True:
#     read input
    input_string = input("> ")
#     tokenize input
    tokens = input_string.split(" ")
#         if the first token is "q":
    if tokens[0] == "q":
#             quit
        print("Goodbye!")
        break
#         else:
    else:
        
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
        if tokens[0] == "pow":
#                   call the power function with the other two tokens
            tokens[2] = float(tokens[2])
            print(power(tokens[1], tokens[2]))

        elif tokens[0] == "add" or tokens[0] == "+":
            print(add(tokens))

        elif tokens[0] == "sub" or tokens[0] == "-":
            print(subtract(tokens))

        elif tokens[0] == "mult" or tokens[0] == "*":
            print(multiply(tokens))

        elif tokens[0] == "div" or tokens[0] == "/":
            tokens[2] = float(tokens[2])
            print(divide(tokens[1], tokens[2]))
        
        elif tokens[0] == "square":
            print(square(tokens[1]))

        elif tokens[0] == "cube":
            print(cube(tokens[1]))
        
        elif tokens[0] == "mod" or tokens[0] == "%":
            tokens[2] = float(tokens[2])
            print(mod(tokens[1], tokens[2]))

