# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        rightView = []

        while queue:

            levelLength = len(queue)
            for level in range(levelLength):
                currentNode = queue.popleft()

                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            rightView.append(currentNode.val)
        return rightView
