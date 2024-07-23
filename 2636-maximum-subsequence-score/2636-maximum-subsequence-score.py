class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs=[(num1,num2) for num1,num2 in zip(nums1,nums2)]
        pairs.sort(key=lambda x:x[1],reverse=True)
        print(pairs)
        minHeap=[]
        maxSum =0
        currentN1Sum = 0
        for eachN1,eachN2 in pairs:
            currentN1Sum += eachN1
            heappush(minHeap,eachN1)

            if len(minHeap) > k:
                currentN1Sum -= heappop(minHeap)
            if len(minHeap) ==k:
                maxSum = max(maxSum, currentN1Sum * eachN2)
        return maxSum