import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class EvalNode(Node):
    def __init__(self,value,left=None, right=None):
        self.left = left
        self.right= right
        self.value = value
    def evaluate(self)->int:
        if self.value.isdigit():
            return self.value
        else:
            leftValue = self.left.evaluate()
            rightValue = self.right.evaluate()
            return Evaluator.calculate(leftValue,rightValue,self.value)
class Evaluator:
    apply={
        '+': lambda a,b: a + b,
        "-": lambda a,b:a-b,
        "*": lambda a,b:a*b,
        "/": lambda a,b:a//b,
    }
    def calculate(operands1,operands2,operator):
        return Evaluator.apply[operator](int(operands1),int(operands2))

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree representing it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack=[]
        for eachToken in (postfix):
            if eachToken.isdigit():
                stack.append(EvalNode(eachToken))
            else:
                operand2,operand1 = stack.pop(),stack.pop()
                stack.append(EvalNode(eachToken,operand1,operand2))
        return stack[0]
        
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        