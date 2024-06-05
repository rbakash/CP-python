class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a,b,c,=0,0,0
        for eachTriplet in triplets:

            # if any of the value is greater than triplet ignore that triplet
            if (
                eachTriplet[0] > target[0]
                or eachTriplet[1] > target[1]
                or eachTriplet[2] > target[2]
            ):
                continue

            a = max(a,eachTriplet[0])
            b=max(b,eachTriplet[1])
            c=max(c,eachTriplet[2])

            if (
               a== target[0]
                and b == target[1]
                and c == target[2]
            ):
                return True

        return False
