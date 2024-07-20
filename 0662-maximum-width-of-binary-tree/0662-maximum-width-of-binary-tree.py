# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        queue = deque()
        queue.append((root,0))
        maxWidth = 0
        while queue:
            currentLevel = len(queue)
            _, firstIndex =queue[0]
            for index in range(currentLevel):
                currentNode,nextIndex = queue.popleft()
                if currentNode.left:
                    queue.append((currentNode.left,2*nextIndex))
                if currentNode.right:
                    queue.append((currentNode.right,2*nextIndex+1))
            maxWidth = max(maxWidth, nextIndex-firstIndex+1)
        return maxWidth
