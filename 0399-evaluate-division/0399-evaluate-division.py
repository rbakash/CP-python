class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        components ={}
       

        def find(node):
            if node not in components:
                components[node]=(node,1)
            parent,weight = components[node]
            if parent != node:
                newParent, newWeight = find(parent)
                components[node]=(newParent,weight*newWeight)
            return components[node]


        def union(node1,node2,value):
            parentOfNode1,weight1 = find(node1)
            parentOfNode2,weight2 = find(node2)

            if parentOfNode1 != parentOfNode2:
                # merge the two
                components[parentOfNode1]=(parentOfNode2,weight2 * value/weight1)

        for (node1,node2),value in zip(equations,values):
            union(node1,node2,value)

        results = []
        for (queryA,queryB) in queries:
            if queryA not in components or queryB not in components:
                results.append(-1.0)
            else:
                nodeA,weightA = find(queryA)
                nodeB,weightB = find(queryB)
                if nodeA != nodeB:
                    results.append(-1.0)
                else:
                    results.append(weightA / weightB)
        return results


            