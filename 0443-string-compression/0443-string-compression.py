class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        start, currentCount, res,end = 0, 1, 0, 0
        while end < len(chars) and start< len(chars):
            print(res, start)
            while ( end + currentCount < len(chars) and
                chars[end + currentCount] == chars[end]
            ):
                currentCount += 1
                # end += 1
            chars[start]=chars[end]
            start+=1
            if currentCount > 1:
                str_repr = str(currentCount)
                chars[start : start + len(str_repr)] = list(str_repr)
                start += len(str_repr)
            end += currentCount
            currentCount = 1
        
        chars=chars[:start]
        return len(chars)
