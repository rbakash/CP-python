class Solution:
    def largestPalindromic(self, num: str) -> str:
        digitFreq = defaultdict(int)
        num = list(num)
        for digit in num:
            digitFreq[(digit)]+=1

        res=[]
        for digit in '9876543210': 
            res.append(digitFreq[digit]//2 * digit)
        mid = ''
        res = "".join(res).lstrip('0')
        
        for digit in digitFreq:
            if digitFreq[digit]%2:
                mid=max(digit,mid)
        print(mid)
        res = res+mid+res[::-1]
        return res if res else '0'