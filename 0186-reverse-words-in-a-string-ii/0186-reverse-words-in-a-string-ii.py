class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start,end =0,0
        s.reverse()
        print(s)
        def reverseWord(start,end):
            while start<=end:
                s[start],s[end] = s[end],s[start]
                start,end=start+1,end-1

        # Reverse the word
        while end < len(s):

            # move the start to space character
            while end < len(s) and s[end]!= " ":
                end+=1
            
            # swap the word
            reverseWord(start,end-1)
           
            start = end+1
            end=start
            # print(s)
        
        