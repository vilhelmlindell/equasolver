def find(string, char):
    return [i for i, ltr in enumerate(string) if ltr == char]

def split_and_remove(string, index):
    before = string[:index]
    after = string[index+1:]
    return before, after

def extract_parentheses(expr, i):
    sides = split_and_remove(expr, i)
    lhs = ""
    rhs = ""

    level = 0

    # check to the left of the operator
    for i in range(len(sides[0]), 0, -1):
        char = sides[0][i - 1]

        if char == ')':
            level += 1
        elif char == '(':
            level -= 1

        # expression can be extracted
        if level == 0:
            lhs = sides[0][i - 1:]
            break

    # check to the right of the operator
    for i in range(len(sides[1])):
        char = sides[1][i]

        if char == '(':
            level += 1
        elif char == ')':
            level -= 1

        # expression can be extracted
        if level == 0:
            rhs = sides[1][:i + 1]
            break

    return lhs, rhs

def parse_expression(expr):
    expr = expr.replace(' ', '')
    i = find(expr, '^')
    sides = extract_parentheses(expr, i)
    parse_expression(sides[0])
    parse_expression(sides[1])
    find(expr, '*')
    find(expr, '/')
    find(expr, '+')
    find(expr, '-')

print(extract_parentheses("5+3*(10-5)", 3))
