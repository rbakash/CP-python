# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue = deque([root])
        isOddLevel = True
        while queue:
            
            level = len(queue)
            isOddLevel = not isOddLevel
            prev = 0
            for index in range(level):
                currentNode = queue.popleft()
                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)

                if not isOddLevel:
                    if not currentNode.val % 2 or (prev and prev >= currentNode.val):
                        return False
                    
                else:
                    # If odd level
                    if currentNode.val % 2 or (prev and prev <= currentNode.val):
                        return False
                prev = currentNode.val
        return True
