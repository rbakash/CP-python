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

        queue = deque([root])
        levelOrder = []
        levelIterator = 0

        while queue:

            levelOrder.append([])
            totalNodes = len(queue)
            for index in range(totalNodes):
                currentNode = queue.popleft()
                levelOrder[levelIterator].append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            levelIterator += 1

        return levelOrder
