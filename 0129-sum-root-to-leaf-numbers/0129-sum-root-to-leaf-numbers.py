# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.totalSum =0
        def rootToNumber(currentNode,result):
        
            if currentNode.left == None and currentNode.right == None:
                self.totalSum+=(result*10+ currentNode.val)
                return
            
            result = result*10+ currentNode.val

            if currentNode.left:
                rootToNumber(currentNode.left,result)

            if currentNode.right:
                rootToNumber(currentNode.right,result)
            
            return
        rootToNumber(root,0)
        return self.totalSum
        