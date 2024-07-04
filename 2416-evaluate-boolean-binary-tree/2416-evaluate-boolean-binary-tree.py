# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    operations:{
        2:"OR",
        3:"AND"
    }
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val ==0 or root.val ==1:
            return root.val
        else:
            leftValue = self.evaluateTree(root.left)
            rightValue = self.evaluateTree(root.right)
            return leftValue or rightValue if root.val == 2 else leftValue and rightValue