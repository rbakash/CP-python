class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        eachSubsetSum = sum(nums)

        if eachSubsetSum % k != 0:
            return False

        eachSubsetSum //= k
        length = len(nums)
        taken = [False] * length
        nums.sort(reverse=True)

        def backtrack(currentSum: int, count: int,currentIndex:int) -> bool:
            if count == 0:
                return True

            if currentSum == eachSubsetSum:
                return backtrack(0, count - 1,0)

            for index in range(currentIndex,length):

                if index > 0 and not taken[index-1] and nums[index-1]==nums[index]:
                    continue
                if taken[index] or currentSum + nums[index]>eachSubsetSum:
                    continue
                else:
                    taken[index] = True
                    if backtrack(currentSum + nums[index], count,index+1):
                        return True
                    taken[index] = False

            return False

        return backtrack(0, k,0)
