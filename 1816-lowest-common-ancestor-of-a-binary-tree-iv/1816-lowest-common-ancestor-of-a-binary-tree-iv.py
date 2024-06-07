# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        visited = set(nodes)

        def dfs(root):
            if root in visited or not root :
                return root
            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root
            if left and not right:
                return left
            if right and not left:
                return right
        return dfs(root)
            
        