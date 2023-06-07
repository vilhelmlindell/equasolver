import expression_parser

class Node:
    element = None
    right=None
    left=None

class Var(Node):
    disallowed_names="*+/%^-"
    numerical = True

    def __eq__(self,other):
        return(self.element==other.element)

    def __init__(self,element):
        if str(element) in self.disallowed_names:
            raise Exception("Ilegall variable name")
        
        self.right = None
        self.left = None

        try:
            self.element = float(element)
        except:
            self.element = element
            self.numerical=False

class Operator(Node):
    allowed_operators=list("*+/%^-=")
    operations=[lambda a,b : a*b,lambda a,b : a+b,lambda a,b : a/b,lambda a,b : a%b,lambda a,b : a**b,lambda a,b : a-b]


    def __eq__(self,other):
        return ((self.element==other.element) and (self.right==other.right) and (self.left==other.left))
        
    def __init__(self,op,left,right):
        if(op not in self.allowed_operators):
            raise Exception("Ilegall operator")
        
        self.left=left
        self.right=right
        self.element=op

    def simplification(self):
        if(type(self.left)==Operator):
            self.left = self.left.simplification()
        if(type(self.right)==Operator):
            self.right = self.right.simplification()
        if(type(self.right)==Var) and (type(self.right)==Var):
            if(self.right.numerical and self.left.numerical):
                return Var(self.perform_op())
        
        if(self.element=="*"):
            #TODO x^2*x simplification
            if(self.right.element==0 or self.left.element==0):
                return Var(0)
            if(self.right.element==1):
                return self.left
            if(self.left.element==1):
                return self.right
            if(self.right==self.left):
                return Operator("^",self.right.element,Var(2))
            
        if(self.element=="/"):
            if(self.right.element==0):
                raise Exception("division by zero encounter")
            if(self.right==self.left):
                return Var(1)
            if(self.left.element==0):
                return Var(0)
            if(self.left.element==1):
                return Operator("^",self.right.element,Var(-1))
            
        
        if(self.element=="+"):
            if(self.right==self.left):
                return Operator("*",self.right.element,Var(2))
            
        if(self.element=="-"):
            if(self.right==self.left):
                return Var(0)
        
        if(self.element=="%"):
            if(int(self.right.element)!=self.right.element or int(self.right.element)!=self.right.element):
                raise Exception("modulo by floats not allowed")
            
        

    def perform_op(self):
        if(self.right.numerical==False or self.left.numerical==False):
            raise Exception("cant perform op on non-numerical")
        return self.operations[self.allowed_operators.index(self.element)](self.left.element,self.right.element)
    


class Expression(Node):
    def __init__(self,input):
        #(self.left,self.right) = expression_parser.parse_expression(input)
        #self.right = 
        self.right = Operator("-",Operator("+",Var("x"),Var("y")),Operator("+",Var("x"),Var("y")))
        self.right = self.right.simplification()
        print(self.right.element)


