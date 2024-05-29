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
        stack = [root]
        parents = {root: None}
        ancestors = []
        nodes = set()
        # nodes.add(root)

        while stack:
            currentNode = stack.pop()
            nodes.add(currentNode)
            if currentNode.left:
                parents[currentNode.left] = currentNode
                stack.append(currentNode.left)

            if currentNode.right:
                parents[currentNode.right] = currentNode
                stack.append(currentNode.right)

        # check if p and q exits
        if p not in nodes or q not in nodes:
            return None

        while p :
            ancestors.append(p)
            p = parents[p]

        while q not in ancestors:
            q = parents[q]

        return q
