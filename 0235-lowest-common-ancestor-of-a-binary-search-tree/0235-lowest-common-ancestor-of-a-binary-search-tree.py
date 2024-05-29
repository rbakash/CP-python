# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        pval = p.val
        qval = q.val
        while node:
            nval = node.val
            if pval > nval and qval > nval: 
                node = node.right
            elif pval < nval and qval < nval: 
                node = node.left
            else:
                return node