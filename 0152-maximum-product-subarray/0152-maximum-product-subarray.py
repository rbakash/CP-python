class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        start, end = 0, 0
        maxProduct = float(-inf)
        prefixProduct=suffixProduct = 1
        for idx in range(len(nums)):
            if prefixProduct == 0:
                prefixProduct =1
            prefixProduct = prefixProduct * nums[idx]
            
            maxProduct = max(prefixProduct, maxProduct)
        print(maxProduct)

        for idx in range(len(nums)-1,-1,-1):
            if suffixProduct == 0:
                suffixProduct =1
            suffixProduct = suffixProduct * nums[idx]
            
            maxProduct = max(suffixProduct, maxProduct)
            # print(suffixProduct,maxProduct)

        
        return maxProduct
