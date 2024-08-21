class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k ==0:
            return -1 if nums1 !=nums2 else 0
        
        toAdd ,toSub = 0,0
        for num1Element, num2Element in zip(nums1,nums2):
            if abs(num1Element- num2Element)%k !=0:
                return -1
            if num1Element > num2Element:
                toAdd  += (num1Element - num2Element)
            else:
                toSub += (num2Element - num1Element)
                
        if toAdd  == toSub:
            return toAdd //k
        else:
            return -1