class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        heap = [(num, idx) for idx, num in enumerate(nums)]
        marked = set()
        ans = []
        totalSum = sum(nums)
        heapify(heap)

        for idx, k in queries:

            if idx not in marked:
                totalSum -= nums[idx]
                marked.add(idx)

            while k > 0 and heap:
                value, minIdx = heappop(heap)
                if minIdx not in marked:
                    totalSum -= value
                    marked.add(minIdx)
                    k -= 1

            ans.append(totalSum)
        return ans
