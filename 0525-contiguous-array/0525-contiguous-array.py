class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        frequency = defaultdict(int)
        # frequency[0] = -1
        count, maxLength = 0, 0

        for index in range(len(nums)):
            if nums[index] == 0:
                count -= 1
            else:
                count += 1
            if count ==0:
                maxLength = index+1
            elif count in frequency:
                maxLength = max(maxLength, (index - frequency[count]))
            else:
                frequency[count] = index
        return maxLength
