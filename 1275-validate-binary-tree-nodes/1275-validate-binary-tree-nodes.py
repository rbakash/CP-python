class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        children = set(leftChild + rightChild)
        root = -1
        seen=set()
        # find the root
        for i in range(n):
            if i not in children:
                root = i
                break

        if root == -1:
            return False

        def dfs(currentNode):
            if currentNode == -1:
                return True
            if currentNode in seen:
                return False
            seen.add(currentNode)
            return dfs(leftChild[currentNode]) and dfs(rightChild[currentNode])

        return dfs(root) and len(seen) == n
