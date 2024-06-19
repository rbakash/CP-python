class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        result =0
        for num in nums:
            maxDigit = 0
            digitCount =0      

            while num > 0:
                maxDigit = max(maxDigit, num%10)
                num=num//10
                digitCount+=1
            for i in range(digitCount):
                num += maxDigit * 10 ** i

            result += num

        return result

        