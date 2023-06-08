from expression import Operator
from expression import Var
from function import Function

FUNCTIONS = [
    "ln",
    "sin",
    "cos",
    "tan",
    "arcsin",
    "arccos",
    "arctan",
    "sinh",
    "cosh",
    "tanh",
    "arcsinh",
    "arccosh",
    "arctanh",
]

OPERATORS = {
    '^': 0,
    '*': 1,
    '/': 2,
    '-': 3,
    '+': 4,
}

def parse_expression(string):
    root_index = 0
    root_precedence = -1
    operator = ''
    has_found = False
    level = 0
    for i in range(len(string)):
        char = string[i]

        if char == '(':
            level += 1
        elif char == ')':
            level -= 1

        if char in OPERATORS and level == 0:
            has_found = True
            precedence = OPERATORS[char]
            if precedence >= root_precedence:
                root_index = i
                root_precedence = precedence
                operator = char

    if not has_found:
        return assign_node(string, False)

    left_operand = string[:root_index]
    right_operand = string[root_index + 1:]

    if left_operand[0] == '(' and left_operand[-1] == ')':
        left_operand = left_operand.strip("()")
    left = assign_node(left_operand, True)

    if right_operand[0] == '(' and right_operand[-1] == ')':
        right_operand = right_operand.strip("()")
    right = assign_node(right_operand, False)

    return Operator(operator, left, right)

def assign_node(expr, right_to_left):
    string = ""
    level = 0

    if right_to_left:
        rang = range(len(expr), -1)
    else:
        rang = range(len(expr))

    for i in rang:
        char = expr[i]

        if char == '(':
            level += 1
        elif char == ')':
            level -= 1

        if char in OPERATORS and level == 0:
            parse_expression(expr)

        if right_to_left:
            string = char + string
        else:
            string = string + char


    for function in FUNCTIONS:
        if string.find(function) == 0:
            string = string[:-1]
            input = string[len(function) + 1:]
            print(input)
            return Function(function, parse_expression(input))

    return Var(expr)
