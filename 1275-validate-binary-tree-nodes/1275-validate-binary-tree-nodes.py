class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def findRoot()-> int:
            children = set(leftChild) | set(rightChild)
    
            for i in range(n):
                if i not in children:
                    return i
            
            return -1
        root = findRoot()
        if root ==-1:
            return False
        stack=[root]
        seen={root}
        while stack:
            currentNode = stack.pop()
            for child in [leftChild[currentNode],rightChild[currentNode]]:
                if child !=-1:
                    if child in seen:
                        return False
                    stack.append(child)
                    seen.add(child)
        return len(seen) ==n