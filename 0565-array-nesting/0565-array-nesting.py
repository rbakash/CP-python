class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        sk=set()
        maxLength = 0
        allsets=defaultdict(int)

        for index in range(len(nums)):
            # sk=set()
            count =0
            while nums[index] not in sk:
                sk.add(nums[index])
                index = nums[index]
                count+=1
            maxLength = max(maxLength, count)
           
        return maxLength