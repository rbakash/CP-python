# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return[]
        queue = deque([root])
        levelIterator = 0
        levelOrders=[]

        while queue:
            levelOrders.append([])
            for index in range(len(queue)):
                currentNode = queue.popleft()
                levelOrders[levelIterator].append(currentNode.val)
                if currentNode.left :
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            levelIterator+=1

        return levelOrders[::-1]