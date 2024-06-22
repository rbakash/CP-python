class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        queue = deque()
        deck.sort()
        result = [0] * N

        for i in range(N):
            queue.append(i)
        
        for card in deck:
            result[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
                
        return result