# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        adjList = defaultdict(int)
        result = []

        def dfs(currentNode):
            if currentNode == None:
                return "*"
            subTree = ("-" + str(currentNode.val) + dfs(currentNode.left) + dfs(currentNode.right))
            adjList[subTree]+=1
            if adjList[subTree] ==2:
                result.append(currentNode)
            return subTree 

        dfs(root)
        return result
