# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        treeIds = defaultdict(int)
        count = defaultdict(int)
        result = []

        def dfs(currentNode):
            if currentNode == None:
                return 0
            triplet = (currentNode.val), dfs(currentNode.left), dfs(currentNode.right)
            if triplet not in treeIds:
                treeIds[triplet] = len(treeIds) + 1
            id = treeIds[triplet]
            count[id] += 1
            if count[id] == 2:
                result.append(currentNode)
            return id

        dfs(root)
        return result
