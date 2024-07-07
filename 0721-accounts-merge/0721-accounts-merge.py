class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        rank = [0] * n
        parent = list(range(n))
 

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

        allEmails={}
        for i in range(n):
            for eachEmail in accounts[i][1:]:
                if eachEmail in allEmails:
                    union(i,allEmails[eachEmail])
                else:
                    allEmails[eachEmail]=i

        emailGroup= defaultdict(list)
        for eachEmail,index in allEmails.items():
            root = find(index)
            emailGroup[root].append(eachEmail)
        answer=[]
        for index,eachGroup in emailGroup.items():
            name = accounts[index][0]
            answer.append([name]+sorted(eachGroup))

        return answer
