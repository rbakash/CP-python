# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # self.previous=None
        # self.successor = None

        # def traversal(root):
        #     if root is None:
        #         return 
        #     traversal(root.left)
        #     if self.previous == p:
        #         self.successor = root
                
        #     self.previous = root
        #     traversal(root.right)
        #     return
        # traversal(root)
        # return self.successor
        succesor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                succesor = root
                root=root.left
        return succesor