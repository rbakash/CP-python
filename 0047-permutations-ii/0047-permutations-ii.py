class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        frequency=defaultdict(int)
        for num in nums:
            frequency[num]+=1
        n = len(nums)
        allPerms=[]
        def backtrack(currentPerm:list)->None:
            if len(currentPerm) == n:
                allPerms.append(currentPerm[:])
                return
            for num in frequency:
                if frequency[num]>0:
                    frequency[num]-=1
                    currentPerm.append(num)
                    backtrack(currentPerm)
                    frequency[num]+=1
                    currentPerm.pop()
            return
        backtrack([])
        return allPerms