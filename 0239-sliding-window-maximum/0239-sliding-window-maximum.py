class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        answer=[]
        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        answer.append(nums[queue[0]])
        for index in range(k,len(nums)):
            if queue and queue[0] == index-k:
                queue.popleft()
            while queue and nums[index] >= nums[queue[-1]]:
                queue.pop()
            queue.append(index)
            answer.append(nums[queue[0]])
            
        return answer