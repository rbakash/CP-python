# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        elements = set(nums)
        prev,current = None,head
        while current:
            if current.val in elements:
                    # need to remove this
                    # if its first element
                if current == head :
                    prev = current
                    current=current.next
                    prev.next=None
                    head = current
                else:
                    current=current.next
                    prev.next.next=None
                    prev.next=current
            else:
                prev =current
                current=current.next

        return head