# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def bstValidHelper( root: Optional[TreeNode], low, high) -> bool:
            if not root:
                return True

            if root.val <= low or root.val >= high:
                return False

            return bstValidHelper( root.left, low, root.val) and bstValidHelper(
                 root.right, root.val, high
            )

        return bstValidHelper( root, -math.inf, math.inf)
