# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0
        def dfsMyVersion(root)->tuple:
            if not root:
                return 0

            leftPath= dfs(root.left)
            rightPath = dfs(root.right)
            if root.val == abs(leftPath[1]) == rightPath[1]:
                self.maxLength = max(self.maxLength, 2+leftPath[0]+rightPath[0])
                return (max(leftPath[0],rightPath[0])+1, root.val)
            if  root.val == leftPath[1] :
                self.maxLength = max(self.maxLength, 1+leftPath[0])
                return ((leftPath[0]+1),root.val)
            if  root.val == rightPath[1] :
                self.maxLength = max(self.maxLength, 1+rightPath[0])
                return ((rightPath[0]+1),root.val)
            return (0,root.val)
        def dfs(root,parent)->int:
            if not root:
                return 0
            leftMaxPath = dfs(root.left,root.val)
            rightMaxPath = dfs(root.right,root.val)
            self.maxLength = max(self.maxLength, leftMaxPath+rightMaxPath)
            return max(leftMaxPath,rightMaxPath)+1 if root.val == parent else 0 
        dfs(root,None)
        return self.maxLength 