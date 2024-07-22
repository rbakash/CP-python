class LockingTree:

    def __init__(self, parent: List[int]):
        self.lockedNodes = defaultdict(int)
        self.parents = parent
        self.tree = [[] for _ in parent]
        for node, nodeParent in enumerate(parent):
            if nodeParent != -1:
                self.tree[nodeParent].append(node)

    def lock(self, num: int, user: int) -> bool:
        if num in self.lockedNodes:
            return False
        self.lockedNodes[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.lockedNodes or self.lockedNodes[num] != user:
            return False
        # print(self.lockedNodes)
        self.lockedNodes.pop(num)
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.lockedNodes:
            return False
        node = num
        # Make sure It does not have any locked ancestors.
        while node != -1:
            if node in self.lockedNodes:
                return False
            node = self.parents[node]

        # Atleast one Locked Descdendant
        lockedDescendant = []
        stack = [num]
        while stack:
            currentNode = stack.pop()
            if currentNode in self.lockedNodes:
                lockedDescendant.append(currentNode)
            for child in self.tree[currentNode]:
                stack.append(child)
        if lockedDescendant:
            self.lockedNodes[num]=user
            for eachLockedDescendant in lockedDescendant:
                self.lockedNodes.pop(eachLockedDescendant)
            return True
        return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
