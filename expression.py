class Node:
    element = None
    right = None
    left = None

    def simplification(self):
        raise NotImplementedError("Method not implemented")


class Var(Node):
    disallowed_names = "*+/%^-"
    numerical = True

    def __eq__(self, other):
        return self.element == other.element

    def __init__(self, element):
        if str(element) in self.disallowed_names:
            raise Exception("Illegal variable name")

        try:
            self.element = float(element)
        except:
            self.element = element
            self.numerical = False

    def simplification(self):
        if self.numerical:
            return self.element
        return self


class Operator(Node):
    allowed_operators = list("*+/%^-=")
    operations = [
        lambda a, b: a * b,
        lambda a, b: a + b,
        lambda a, b: a / b,
        lambda a, b: a % b,
        lambda a, b: a**b,
        lambda a, b: a - b,
    ]

    def __eq__(self, other):
        return (
            (self.element == other.element)
            and (self.right == other.right)
            and (self.left == other.left)
        )

    def __init__(self, op, left, right):
        if op not in self.allowed_operators:
            raise Exception("Illegal operator")

        self.left = left
        self.right = right
        self.element = op

    def simplification(self):
        self.right = self.right.simplification()
        self.left = self.left.simplification()

        if isinstance(self.right, Var) and isinstance(self.left, Var):
            if self.right.numerical and self.left.numerical:
                return Var(self.perform_op())

        if self.element == "*":
            # TODO: x^2*x simplification
            if self.right.element == 0 or self.left.element == 0:
                return Var(0)
            if self.right.element == 1:
                return self.left
            if self.left.element == 1:
                return self.right
            if self.right == self.left:
                return Operator("^", self.right.element, Var(2))

        if self.element == "/":
            if self.right.element == 0:
                raise Exception("Division by zero encountered")
            if self.right == self.left:
                return Var(1)
            if self.left.element == 0:
                return Var(0)
            if self.left.element == 1:
                return Operator("^", self.right.element, Var(-1))

        if self.element == "+":
            if self.right == self.left:
                return Operator("*", self.right.element, Var(2))

        if self.element == "-":
            if self.right == self.left:
                return Var(0)

        if self.element == "%":
            if (
                int(self.right.element) != self.right.element
                or int(self.right.element) != self.right.element
            ):
                raise Exception("Modulo by floats not allowed")

        return self

    def perform_op(self):
        if not self.right.numerical or not self.left.numerical:
            raise Exception("Cannot perform operation on non-numerical values")
        return self.operations[self.allowed_operators.index(self.element)](
            self.left.element, self.right.element
        )
