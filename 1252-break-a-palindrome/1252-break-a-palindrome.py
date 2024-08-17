class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) ==1:
            return ""
        string = list(palindrome)
        right =len(string)-1
        for left in range(len(palindrome)):
            if string[left]!="a" and string[right]!="a" and left!=right:
                string[left]="a"
                break
            else:
                right-=1
        print(right,left)
        if left >right:
            string[len(string)-1]="b"
        return "".join(string)