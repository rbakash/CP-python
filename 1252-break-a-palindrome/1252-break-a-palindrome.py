class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) ==1:
            return ""
        string = list(palindrome)
        right =len(string)-1
        for index in range(len(palindrome)):
            if string[index]!="a" and string[right]!="a" and index!=right:
                string[index]="a"
                break
            else:
                right-=1
        print(right,index)
        if index == right:
            string[left]="b"
        if index >right:
            string[len(string)-1]="b"
        return "".join(string)