class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        eachSubsetSum = sum(nums)

        if eachSubsetSum % k != 0:
            return False

        eachSubsetSum //= k
        length = len(nums)
        taken = ['0'] * length
        nums.sort(reverse=True)
        triedSubsets={}

        def backtrack(currentSum: int, count: int,currentIndex:int) -> bool:
            if count == k - 1:
                return True
            if currentSum > eachSubsetSum:
                return False
            currentSubset="".join(taken)
            if currentSubset in triedSubsets:
                return triedSubsets[currentSubset]

            if currentSum == eachSubsetSum  :
                triedSubsets[currentSubset] = backtrack(0, count + 1,0)
                return triedSubsets[currentSubset]

            for eachNum in range(currentIndex,length):

                if taken[eachNum] =='0':
                    taken[eachNum] = '1'
                    # print("backTrack")

                    if backtrack(currentSum + nums[eachNum], count,eachNum+1):
                        return True
                    taken[eachNum] = '0'

            triedSubsets[currentSubset] = False
            return False

        return backtrack(0, 0,0)
