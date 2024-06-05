class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start,end =0,0
        partition = []

        # find the last occurence of all characters
        lastOccurence={}
        for index,character in enumerate(s):
            lastOccurence[character]= index
        print(lastOccurence)
        for index,character in enumerate(s):
            end = max(end,lastOccurence[character])
            if end == index:
                partition.append(end-start+1)
                start=end+1
                end=end+1

        return partition
 
        