class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isPalindrome(string):
            return string == string[::-1]

        # Both palindrome
        if isPalindrome(a) and isPalindrome(b):
            return True

        def check(a: str, b: str) -> bool:
            pointerA, pointerB = 0, len(a) - 1
            while pointerA < pointerB and a[pointerA] == b[pointerB]:
                pointerA += 1
                pointerB -= 1
            s1, s2 = a[:pointerA] + b[pointerA:], a[: pointerB + 1] + b[pointerB + 1 :]
            return isPalindrome(s1) or isPalindrome(s2)

        return check(a, b) or check(b, a)
