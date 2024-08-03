# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        current=head
        newList = None
        newHead=None
        stack=[]
        currentK=0
        def reverse(isReverse:bool = True):
            nonlocal newList, newHead
            while stack:
                    currentNode = stack.pop()
                    newNode = ListNode(currentNode)
                    if newList is not None:
                        newList.next=newNode
                        newList = newList.next
                    else:
                        newHead = newNode
                        newList = newNode
        while current:
            if currentK ==k:
                # WHen we have enough nodes
                reverse()
                currentK=0
            else:
                stack.append(current.val)
                currentK+=1
                current = current.next
        # copy the remaing item without reversing
        if currentK ==k:
            reverse()
        else:
            # copy
            for index in range(len(stack)):
                newNode = ListNode(stack[index])
                if newList is not None:
                    newList.next=newNode
                    newList = newList.next
                else:
                    newHead = newNode
                    newList = newNode
        return newHead