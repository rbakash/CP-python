# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >=0

    def height(self, root: Optional[TreeNode]) ->  int:
        if root is None:
            return 0

        LeftHeight, rightHeight = self.height(root.left), self.height(root.right)
        if LeftHeight < 0 or rightHeight < 0 or abs(LeftHeight - rightHeight) > 1:
            return -1
        return max(LeftHeight, rightHeight) + 1
