class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # subsets = [[]]
        # for num in nums:
        #     for eachSubset in subsets:
        #         subsets.append(eachSubset+[num])

        # return subsets

        subset = []
        # currentSubset = []

        def dfs(index,currentSubset):
            if index == len(nums):
                subset.append(currentSubset[:])
                return

            # decision to include the current character
            currentSubset.append(nums[index])
            dfs(index + 1,currentSubset)

            # decision to not include the current character
            currentSubset.pop()
            dfs(index + 1,currentSubset)

        dfs(0,[])
        return subset
