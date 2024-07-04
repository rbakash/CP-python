class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        newArray = nums.copy()
        for index in range(n-1):
            temp = []
            for iterator in range(len(newArray)-1):
                temp.append((newArray[iterator] + newArray[iterator + 1])%10)
                # print(temp)
            newArray = temp.copy()
        # print(newArray)
        return newArray[0]
