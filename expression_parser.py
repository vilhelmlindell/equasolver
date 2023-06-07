#from expression import *

OPERATORS = "^*/-+"

def parse_expression(expr) -> Operator
    expr = expr.replace(' ', '')
    level = 0
    operator_indices = [[]] * 5
    for i in range(len(expr)):
        char = expr[i]

        if char == '(':
            level += 1
        elif char == ')':
            level -= 1

        if level != 0:
            continue

        if char == '^':
            operator_indices[0].append(i)
        elif char == '*':
            operator_indices[1].append(i)
        elif char == '/':
            operator_indices[2].append(i)
        elif char == '-':
            operator_indices[3].append(i)
        elif char == '+':
            operator_indices[4].append(i)

    for operator in range(len(operator_indices)):
        for i in range(len(operator_indices[operator]), -1):
            #node = Operator(OPERATORS[i])
            operands = adjacent_operands(expr, i)

            if operands[0][-1] == ')':
                node.left = parse_expression(operands[0])
            else:
                node.left = Var(operands[0])

            if operands[1][0] == '(':
                node.right = parse_expression(operands[1])
            else:
                node.right = Var(operands[1])

def adjacent_operands(string, index):
    sides = split_and_remove(string, index)
    lhs = ""
    rhs = ""
    
    has_found = False
    level = 0

    # Extract expression to the left of the operator
    for i in range(len(sides[0]), 0, -1):
        char = sides[0][i - 1]

        if char == ')':
            level += 1
            has_found = True
        elif char == '(':
            level -= 1

        if level == 0:
            if has_found:
                lhs = sides[0][i - 1:]
                break
            elif OPERATORS.find(char) != -1:
                lhs = sides[0][i:]
                break

    has_found = False
    level = 0

    # Extract expression to the right of the operator
    for i in range(len(sides[1])):
        char = sides[1][i]

        if char == '(':
            has_found = True
            level += 1
        elif char == ')':
            level -= 1

        if level == 0:
            if has_found:
                rhs = sides[1][:i + 1]
                break
            elif OPERATORS.find(char) != -1:
                rhs = sides[1][:i]
                break

    return lhs, rhs

def find(string, char):
    return [i for i, ltr in enumerate(string) if ltr == char]

def split_and_remove(string, index):
    before = string[:index]
    after = string[index+1:]
    return before, after

print(adjacent_operands("5+323+123*1034-5+3", 9))
