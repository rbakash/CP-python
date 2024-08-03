class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence=[nums[0]]

        for num in nums[1:]:
            if num > subsequence[-1]:
                subsequence.append(num)
            else:
                # find the existing number to replace with num as 
                # that will give num - replace num distance
                index =0
                while num > subsequence[index]:
                    index+=1
                # subsequence.insert(index,num)
                subsequence[index]=num
        return len(subsequence)