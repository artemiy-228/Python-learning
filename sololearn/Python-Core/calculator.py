def cout():
    x, y, z = map(str, input("Enter your mathematical expression: ").split())
    return [x, y, z]


def expression(expr):
    if expr[1] == "+":
        print(int(expr[0]) + int(expr[2]))
    elif expr[1] == "-":
        print(int(expr[0]) - int(expr[2]))
    elif expr[1] == "*":
        print(int(expr[0]) * int(expr[2]))
    elif expr[1] == "/":
        print(int(expr[0]) / int(expr[2]))
    elif expr[1] == "//":
        print(int(expr[0]) // int(expr[2]))
    elif expr[1] == "%":
        print(int(expr[0]) % int(expr[2]))
    else:
        print("Incorrect operand")

while True:
    try:
        expr = cout()
        expression(expr)
    except ValueError:
        print("Incorrect operand", "Hint: if you enter it properly, input space's between numbers and operand", sep="\n")