class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hmap = {}

        hmap = Counter(nums)

        print(hmap)

        sortedmap = sorted(hmap.items(), key=lambda items : items[1], reverse=True)
        res = []
        print(sortedmap)
        for i in range(len(sortedmap)):
        
            if k>0:
                res.append(sortedmap[i][0])
                k-=1

        return res