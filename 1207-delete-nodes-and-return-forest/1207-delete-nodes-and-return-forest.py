# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        toDelete= set(to_delete)
        forest =[]
        def postOrder(currentNode):
            if not currentNode:
                return None
            currentNode.left = postOrder(currentNode.left)
            currentNode.right = postOrder(currentNode.right)

            if currentNode.val in toDelete:
                if currentNode.left:
                    forest.append(currentNode.left)
                if currentNode.right:
                    forest.append(currentNode.right)
                return None
            return currentNode
        root = postOrder(root)
        if root:
            forest.append(root)
        
        return forest

