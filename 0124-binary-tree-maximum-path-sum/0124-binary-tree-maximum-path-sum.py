# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSum=float("-inf")
        def dfs(root):
            if not root:
                return 0
            
            leftMaxSum = max(dfs(root.left),0)
            rightMaxSum = max(dfs(root.right),0)
            self.maxPathSum = max(self.maxPathSum, leftMaxSum+rightMaxSum+root.val)

            return root.val + max(leftMaxSum,rightMaxSum)
        dfs(root)
        return self.maxPathSum 