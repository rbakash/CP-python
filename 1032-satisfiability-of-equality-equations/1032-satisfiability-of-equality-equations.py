class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        parent = [i for i in range(26)]
        rank = [0] * 26

        def find(nodeX):
            if nodeX != parent[nodeX]:
                parent[nodeX] = find(parent[nodeX])
            return parent[nodeX]

        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            if parent1 != parent2:
                if rank[parent1] > rank[parent2]:
                    parent[parent2] = parent1
                elif rank[parent2] > rank[parent1]:
                    parent[parent1] = parent2
                else:
                    parent[parent2] = parent1
                    rank[parent1] += 1
                    return False
            return True

        for eachEquation in equations:
            node1, node2, equation = (
                ord(eachEquation[0]) - 97,
                ord(eachEquation[3]) - 97,
                eachEquation[1],
            )
            if equation == "=":
                union(node1, node2)
        for eachEquation in equations:
            node1, node2, equation = (
                ord(eachEquation[0]) - 97,
                ord(eachEquation[3]) - 97,
                eachEquation[1],
            )
            if equation == "!":
                if find(node1) == find(node2):
                    return False
        return True
