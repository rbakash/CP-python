# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longestDiameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.findLongestDiameter(root, 0)
        return self.longestDiameter

    def findLongestDiameter(self, root: Optional[TreeNode], currentDiameter) -> int:
        if root is None:
            return 0

        leftDiameter = self.findLongestDiameter(root.left, currentDiameter + 1)
        rightDiameter = self.findLongestDiameter(root.right, currentDiameter + 1)
        self.longestDiameter = max(self.longestDiameter, leftDiameter + rightDiameter)
        return max(leftDiameter, rightDiameter) + 1
