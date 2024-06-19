class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        heap =[(num,idx) for idx,num in enumerate(nums)]
        marked=set()
        ans =[]
        totalSum =sum(nums)
        heapify(heap)
        
        for idx, k in queries:

            if idx not in marked:
                totalSum -= nums[idx]
                marked.add(idx)
            
            while k > 0 and heap:

                if heap[0][1] not in marked:
                    totalSum -= heap[0][0]
                    marked.add(heap[0][1])
                    heappop(heap)
                    k-=1
                else: 
                    heappop(heap)
            ans.append(totalSum)
        return ans
        
        