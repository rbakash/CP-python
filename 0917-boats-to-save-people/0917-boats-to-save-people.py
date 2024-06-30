class Solution:
    def numRescueBoats(self, peoples: List[int], limit: int) -> int:
        end, minimumBoat,start = len(peoples)-1, 0,0
        peoples.sort()
        while start<= end:
            if peoples[start]+peoples[end] <=limit:
                # 2 people can be accomodated in the boat
                start+=1
            end-=1
            minimumBoat+=1
        return minimumBoat
