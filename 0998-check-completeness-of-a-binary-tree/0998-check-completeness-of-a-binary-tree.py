# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        nullFound = False
        while queue:
            currentNode = queue.popleft()
            if currentNode == None:
                nullFound = True
            else:
                if nullFound:
                    return False
                queue.append(currentNode.left)
                queue.append(currentNode.right)
        return True
