class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        start, currentCount,res = 0,  1, 0
        while start < len(chars):
            print(res, start)
            while start + currentCount < len(chars) and chars[start + currentCount] == chars[start]:
                currentCount += 1
                # end += 1
            chars[res] = chars[start]
            res += 1
            if currentCount > 1:
                str_repr = str(currentCount)
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr)
            start += currentCount
            currentCount=1
        return res
