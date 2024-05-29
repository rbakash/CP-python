# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = collections.deque()
        queue.append(root)
        levelOrder = []

        while queue:

            level = []
            totalNodes = len(queue)
            for index in range(totalNodes):
                currentNode = queue.popleft()
                level.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            levelOrder.append(level)

        return levelOrder
