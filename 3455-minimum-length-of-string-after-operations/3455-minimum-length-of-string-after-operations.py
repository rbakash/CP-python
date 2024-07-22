class Solution:
    def minimumLength(self, s: str) -> int:

        frequency=defaultdict(list)
        for index,character in enumerate(s):
            frequency[character].append(index)
        
        minLength =0
        for key,indexes in frequency.items():
            if len(indexes) > 2:
               
                # remove the 2 indices starting from 1 index
                if len(indexes) % 2 == 0:
                    minLength += 2
                else:
                    minLength += 1
            else:
                minLength +=len(indexes)
            # del frequency[key]
        
        return minLength

