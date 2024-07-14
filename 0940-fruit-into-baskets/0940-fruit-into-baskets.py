class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxTrees, start = 0, 0
        basket = defaultdict(int)
        for end, fruit in enumerate(fruits):
            basket[fruit] += 1
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
            maxTrees = max(maxTrees, end - start + 1)
        return maxTrees
