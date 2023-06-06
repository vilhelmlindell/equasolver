import expression_parser

class Node:
    element = None
    right=None
    left=None

class Var(Node):
    disallowed_names="*+/%^-"
    numerical = True

    def __init__(self,element):
        if element in self.disallowed_names:
            raise Exception("Ilegall variable name")
        
        self.right = None
        self.left = None

        try:
            self.element = float(element)
        except:
            self.element = element
            self.numerical=False

class Operator(Node):
    op=None
    allowed_Operators="*+/%^-"
    operations=[lambda a,b : a*b,lambda a,b : a+b,lambda a,b : a/b,lambda a,b : a%b,lambda a,b : a**b,lambda a,b : a-b]

    def __init__(self,op,left,right):
        if(left == None or right == None):
            raise Exception("Operators must have a two defined nodes")
        if(op not in self.allowed_Operators):
            raise Exception("Ilegall operator")
        
        self.left=left
        self.right=right
        self.op=op

    def simplification(self):
        if(type(self.left)==Operator):
            self.left = self.left.simplification()
        if(type(self.right)==Operator):
            self.right = self.right.simplification()

        if(self.right.numerical and self.left.numerical):
            return Var(self.perform_op())
        
        if(self.op=="*"):
            #TODO x^2*x simplification
            if(self.right.element==0 or self.left.element==0):
                return Var(0)
            if(self.right.element==1):
                return self.left
            if(self.left.element==1):
                return self.right
            if(self.right.element==self.left.element):
                return Operator("^",self.right.element,Var(2))
            
        if(self.op=="/"):
            if(self.right.element==0):
                raise Exception("division by zero encounter")
            if(self.right.element==self.left.element):
                return Var(1)
            if(self.left.element==0):
                return Var(0)
            if(self.left.element==1):
                return Operator("^",self.right.element,Var(-1))
            
        
        if(self.op=="+"):
            if(self.right.element==self.left.element):
                return Operator("*",self.right.element,Var(2))
            
        if(self.op=="-"):
            if(self.right.element==self.left.element):
                return Var(0)
        
        if(self.op=="%"):
            if(int(self.right.element)!=self.right.element or int(self.right.element)!=self.right.element):
                raise Exception("modulo by floats not allowed")
            
        

    def perform_op(self):
        if(self.right.numerical==False or self.left.numerical==False):
            raise Exception("cant perform op on non-numerical")
        return self.operations[self.operations.index(self.op)](self.left.element,self.right.element)
    


class Expression:
    root=None
    def __init__(self,input):
        self.root = expression_parser.parse_expression(input)
        

