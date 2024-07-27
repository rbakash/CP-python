class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word for word in s.split(" ") if word !=""]
        print(words[::-1])
        return " ".join(words[::-1])