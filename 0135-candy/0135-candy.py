class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies=[1]*len(ratings)
        for index in range(1,len(ratings)):
            if ratings[index]> ratings[index-1]:
                candies[index] = candies[index-1]+1
        
        for index in range(len(ratings)-1,0,-1):
            if ratings[index-1]> ratings[index]:
                candies[index-1] = max(candies[index]+1,candies[index-1] )

        return sum(candies)
        
