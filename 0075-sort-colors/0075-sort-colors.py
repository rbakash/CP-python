class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroIndex = 0
        n = len(nums)
        secondIndex = n-1
        iterator =0
        while iterator <= secondIndex:
            if nums[iterator] == 0:
                nums[zeroIndex], nums[iterator] = nums[iterator], nums[zeroIndex]
                zeroIndex += 1
                iterator+=1
            elif nums[iterator] == 2:
                nums[secondIndex], nums[iterator] = nums[iterator], nums[secondIndex]
                secondIndex -= 1
            else : iterator+=1

        return None
