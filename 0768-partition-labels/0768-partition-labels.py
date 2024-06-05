class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size,end =0,0
        partition = []

        # find the last occurence of all characters
        lastOccurence={}
        for index,character in enumerate(s):
            lastOccurence[character]= index

        for index,character in enumerate(s):
            end = max(end,lastOccurence[character])
            size+=1
            if end == index:
                partition.append(size)
                # start=end+1
                size=0
                end=end+1

        return partition
 
        