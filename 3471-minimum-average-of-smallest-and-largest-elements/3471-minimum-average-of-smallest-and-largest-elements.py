class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages=float("inf")
        nums.sort()
        n = len(nums)
        for index in range(0,n//2):
           avg = ((nums[index]+nums[n-index-1])/2)
           averages = min(averages, avg)
        return averages

        