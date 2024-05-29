# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        parents = {root: None}

        stack = []
        treeIterator = root
        stack.append(root)

        while p not in parents or q not in parents:
            currentNode = stack.pop()
            if currentNode.left:
                parents[currentNode.left] = currentNode
                stack.append(currentNode.left)
            if currentNode.right:
                parents[currentNode.right] = currentNode
                stack.append(currentNode.right)

        ancestors = set()

        while p:
            ancestors.add(p)
            p = parents[p]

        while q not in ancestors:
            q = parents[q]

        return q
