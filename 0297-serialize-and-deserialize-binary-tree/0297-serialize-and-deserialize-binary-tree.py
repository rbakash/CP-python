# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        levelOrder =[]
        queue=deque([root])
        while queue:
            currentNode = queue.popleft()
            
            if currentNode:
                levelOrder.append(str(currentNode.val))
                queue.append(currentNode.left)
                queue.append(currentNode.right)
            else:
                levelOrder.append("None")
        print(",".join(levelOrder))
        return ",".join(levelOrder)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="None":
            return None
        data=data.split(",") 
        root = TreeNode(int(data[0]))
        queue = deque([root])
        index =1
        while queue:
            currentNode = queue.popleft()
            if index < len(data):
                if data[index] !="None":
                    leftVal = data[index]
                    leftNode = TreeNode(leftVal)
                    currentNode.left = leftNode
                    queue.append(leftNode)
                index+=1
            if index < len(data):
                if data[index] !="None":
                    rightVal = data[index]
                    rightNode = TreeNode(rightVal)
                    currentNode.right = rightNode
                    queue.append(rightNode)
                index+=1
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))