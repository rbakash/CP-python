class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k ==0:
            return -1 if nums1 !=nums2 else 0
        positiveDiff,negativeDiff = 0,0
        for num1Element, num2Element in zip(nums1,nums2):
            if num1Element > num2Element:
                if (num1Element - num2Element)%k ==0:
                    positiveDiff += (num1Element - num2Element)
                else:
                    return -1
            else:
                if (num2Element - num1Element)%k ==0:
                    negativeDiff += (num2Element - num1Element)
                else:
                    return -1
        if positiveDiff == negativeDiff:
            return positiveDiff//k
        else:
            return -1