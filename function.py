import math 
from expression import Node

FUNCTIONS = {
    "ln": lambda x: math.log(x, math.e),
    "sin": lambda x: math.sin(x),
    "cos": lambda x: math.cos(x),
    "tan": lambda x: math.tan(x),
    "arcsin": lambda x: math.asin(x),
    "arccos": lambda x: math.acos(x),
    "arctan": lambda x: math.atan(x),
    "sinh": lambda x: math.sinh(x),
    "cosh": lambda x: math.cosh(x),
    "tanh": lambda x: math.tanh(x),
    "arcsinh": lambda x: math.asinh(x),
    "arccosh": lambda x: math.acosh(x),
    "arctanh": lambda x: math.atanh(x),
}

class Function(Node):
    function = ""
    left = None
    right = None

    def __init__(self, function, input):
        if function not in FUNCTIONS:
            raise Exception("Not a built in function")
        self.function = function
        self.element = input
