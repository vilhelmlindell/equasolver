from expression import Operator
from expression import Var

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
    level = 0
    for i in range(len(string)):
        char = string[i]

        if char == '(':
            level += 1
        elif char == ')':
            level -= 1

        if char in OPERATORS and level == 0:
            precedence = OPERATORS[char]
            if precedence >= root_precedence:
                root_index = i
                root_precedence = precedence
                operator = char

    left_operand = string[:root_index]
    right_operand = string[root_index + 1:]

    if is_var(left_operand, True):
        left = Var(left_operand)
    else:
        if left_operand[0] == '(' and left_operand[-1] == ')':
            left_operand = left_operand.strip("()")
        left = parse_expression(left_operand)

    if is_var(right_operand, False):
        right = Var(right_operand)
    else:
        if right_operand[0] == '(' and right_operand[-1] == ')':
            right_operand = right_operand.strip("()")
        right = parse_expression(right_operand)

    return Operator(operator, left, right)

def is_var(string, right_to_left):
    if string[0] == '(' and string[-1] == ')':
        return False

    if right_to_left:
        for i in range(len(string), -1):
            char = string[i]
            if char in OPERATORS:
                return False
    else:
        for i in range(len(string)):
            char = string[i]
            if char in OPERATORS:
                return False

    return True
