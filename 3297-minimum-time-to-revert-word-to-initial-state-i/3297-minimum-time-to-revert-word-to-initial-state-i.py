class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        time =1
        for i in range(k, n, k):
            if word[i:] == word[:n-i]:
                break
            time+=1
        return time