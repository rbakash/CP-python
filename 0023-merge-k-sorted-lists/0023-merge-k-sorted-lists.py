# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class HeapNode:
    def __init__(self,node):
        self.node = node
    def __lt__(self,other):
        return self.node.val < other.node.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #---------using Min Heap
        dummyNode = ListNode(0)
        current=dummyNode
        minHeap = []
        for eachList in lists:
            if eachList:
                heappush(minHeap,HeapNode(eachList))
        while minHeap:
            print(minHeap[0].node.val)
            currentNode = heappop(minHeap)
            currentNode = currentNode.node
            current.next = currentNode
            current= current.next
            if currentNode.next:
                heappush(minHeap,HeapNode(currentNode.next))
        return dummyNode.next
            
        # ------ Normal linked list swapping ------- 
        # listLength = len(lists)
        
        # if listLength == 0:
        #     return None
        
        # if listLength == 1:
        #     return None if (not lists[0]) else lists[0] 
        
        # prev=lists[0]

        # def mergeTwoLists(list1:List[ListNode],list2:[List[ListNode]]):

        #     if list1 is None:
        #         return list2
        #     elif list2 is None:
        #         return list1
        #     #keep joining smaller values in comparision to other list
        #     elif list1.val > list2.val:
        #         list2.next = mergeTwoLists(list1, list2.next)
        #         return list2
        #     else:
        #         list1.next = mergeTwoLists(list1.next, list2)
        #         return list1
        # for index in range(1,listLength):
        #     prev = mergeTwoLists(prev,lists[index])
        # return prev