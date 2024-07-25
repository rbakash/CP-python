# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        prevTrees={
            0:[],
            1:[TreeNode()]
        }
        def dfs(nodes):
            # Definition for a binary tree node.
            if nodes in prevTrees:
                return prevTrees[nodes]

            res = []
            for i in range(1, nodes, 2):
                left,right  = dfs(i), dfs(nodes - i - 1)

                for l in left:
                    for r in right:
                        root = TreeNode(0, l, r)
                        res.append(root)
            prevTrees[nodes]=res
            return res
        
        return dfs(n)
