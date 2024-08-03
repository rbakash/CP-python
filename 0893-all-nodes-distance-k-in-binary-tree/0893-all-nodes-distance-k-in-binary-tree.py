# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Build the graph to include root edge along with left,right
        parent = defaultdict(int)
        
        def createGraph():
            stack = [root]
            while stack:
                currentNode = stack.pop()
                if currentNode.left:
                    parent[currentNode.left] = currentNode
                    stack.append(currentNode.left)
                if currentNode.right:
                    parent[currentNode.right] = currentNode
                    stack.append(currentNode.right)

        createGraph()
        nodesAtKthDistance = []
        visited = set()

        # Use the graph to traverse the tree
        def dfs(root, currentDistance):
            if not root or root in visited:
                return

            visited.add(root)
            if currentDistance == k:
                nodesAtKthDistance.append(root.val)
                return

            for eachNode in [root.left, root.right, parent[root]]:

                if eachNode and eachNode.val not in visited:

                    dfs(eachNode, currentDistance + 1)

            return

        dfs(target, 0)
        return nodesAtKthDistance
