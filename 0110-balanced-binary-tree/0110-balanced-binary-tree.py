# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root)[0]

    def height(self, root: Optional[TreeNode]) -> (bool, int):
        if root is None:
            return True, -1

        leftBalanced, LeftHeight = self.height(root.left)
        if not leftBalanced:
            return False, 0

        rightBalanced, rightHeight = self.height(root.right)
        if not rightBalanced:
            return False, 0
        return (abs(LeftHeight - rightHeight) < 2), max(LeftHeight, rightHeight) + 1
