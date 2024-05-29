# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([[root, -9999999999]])
        numberOfGoodNodes = 0

        while queue:
            levelLength = len(queue)

            for index in range(levelLength):
                currentNode, currentMax = queue.popleft()
                if currentMax <= currentNode.val:
                    numberOfGoodNodes += 1
                    currentMax = currentNode.val
                if currentNode.left:
                    queue.append(
                        [
                            currentNode.left,
                            (
                                currentNode.left.val
                                if currentMax < currentNode.left.val
                                else currentMax
                            ),
                        ]
                    )

                if currentNode.right:
                    queue.append(
                        [
                            currentNode.right,
                            (
                                currentNode.right.val
                                if currentMax < currentNode.right.val
                                else currentMax
                            ),
                        ]
                    )

        return numberOfGoodNodes
