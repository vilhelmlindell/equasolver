
class node:
    element = None
    right=None
    left=None

class var(node):
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

class operator(node):
    op=None
    allowed_operators="*+/%^-"
    operations=[lambda a,b : a*b,lambda a,b : a+b,lambda a,b : a/b,lambda a,b : a%b,lambda a,b : a**b,lambda a,b : a-b]

    def __init__(self,op,left,right):
        if(left == None or right == None):
            raise Exception("operators must have a two defined nodes")
        if(op not in self.allowed_operators):
            raise Exception("Ilegall operator")
        
        self.left=left
        self.right=right
        self.op=op

    def simplification(self):
        if(type(self.left)==operator):
            self.left = self.left.simplification()
        if(type(self.right)==operator):
            self.right = self.right.simplification()

        if(self.right.numerical and self.left.numerical):
            return var(self.perform_op())
        
        if(self.op=="*"):
            #TODO x^2*x simplification
            if(self.right.element==0 or self.left.element==0):
                return var(0)
            if(self.right.element==1):
                return var(self.left.element)
            if(self.left.element==1):
                return var(self.right.element)
            if(self.right.element==self.left.element):
                return operator("^",self.right.element,2)
            
        if(self.op=="/"):
            if(self.right.element==self.left.element):
                return var(1)
            
        
        if(self.op=="+"):
            if(self.right.element==self.left.element):
                return operator("*",self.right.element,2)
            
        if(self.op=="-"):
            if(self.right.element==self.left.element):
                return var(0)
            



    def perform_op(self):
        if(self.right.numerical==False or self.left.numerical==False):
            raise Exception("cant perform op on non-numerical")
        return self.operations[self.operations.index(self.op)](self.left.element,self.right.element)
    

        





class expression:
