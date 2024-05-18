class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right = [0] * length, [0] * length

        iterator = 1
        # initialize the left product to 1
        left[0] = 1
        while iterator < length:
            left[iterator] = left[iterator - 1] * nums[iterator - 1]
            iterator += 1

        

        right[length - 1] = 1
        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

       

        ans = [0]*length

        for i in range(length):
            ans[i]=(left[i] * right[i])
           

        return ans
