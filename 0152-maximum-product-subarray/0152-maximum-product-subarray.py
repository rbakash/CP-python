class Solution:
    def maxProduct(self, nums: List[int]) -> int:
       
        maxProduct = float(-inf)
        prefixProduct = suffixProduct = 1
        n = len(nums)
        
        for idx in range(len(nums)):
            if prefixProduct == 0:
                prefixProduct = 1
            if suffixProduct == 0:
                suffixProduct = 1
            prefixProduct = prefixProduct * nums[idx]
            suffixProduct = suffixProduct * nums[n - idx - 1]
            maxProduct = max(prefixProduct,suffixProduct, maxProduct)

        return maxProduct
