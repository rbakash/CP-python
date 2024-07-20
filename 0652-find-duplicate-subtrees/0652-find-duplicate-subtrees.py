# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        adjList = defaultdict(int)
        count=defaultdict(int)
        result = []

        def dfs(currentNode):
            if currentNode == None:
                return 0
            subTree = (currentNode.val),dfs(currentNode.left),dfs(currentNode.right)
            if subTree not in adjList:
                adjList[subTree]= len(adjList)+1
            id = adjList[subTree]
            count[id]+=1
            if count[id] ==2:
                result.append(currentNode)
            return id 

        dfs(root)
        return result
