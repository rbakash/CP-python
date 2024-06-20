class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def add(self,node):
        # Move the node to the end
        previousEnd = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

        node.prev = previousEnd
        previousEnd.next = node
        
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node =self.map[key]
        self.remove(node)
        self.add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        
        node = ListNode(key,value)
        self.map[key] = node
        self.add(node)

        # if we are over the capacity
        if len(self.map) > self.capacity:
            # Delete the first node
            nodeToDelete = self.head.next
            self.remove(nodeToDelete)
            del self.map[nodeToDelete.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)