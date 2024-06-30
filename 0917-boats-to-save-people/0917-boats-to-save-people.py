class Solution:
    def numRescueBoats(self, peoples: List[int], limit: int) -> int:
        end, minimumBoat,start = len(peoples)-1, 0,0
        peoples.sort()
        while peoples[end] == limit:
            minimumBoat += 1
            end -= 1
        # When start equals end, it means only one person is left to be considered.
        # This person still needs a boat, so the loop should process this case to ensure they are not skipped
        while start<= end:
            if peoples[start]+peoples[end] <=limit:
                # 2 people can be accomodated in the boat
                start+=1
            end-=1
            minimumBoat+=1
        return minimumBoat
