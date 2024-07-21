# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(currentNode) -> list:
            if not currentNode:
                return (0, 0)

            leftMaxWithRoot, leftMaxWithoutRoot = dfs(currentNode.left)
            rightMaxWithRoot, rightMaxWithoutRoot = dfs(currentNode.right)
            robTheRoot = currentNode.val + leftMaxWithoutRoot + rightMaxWithoutRoot
            robChild = max(leftMaxWithRoot, leftMaxWithoutRoot) + max(
                rightMaxWithRoot, rightMaxWithoutRoot
            )
            return [robTheRoot, robChild]

        return max(dfs(root))
