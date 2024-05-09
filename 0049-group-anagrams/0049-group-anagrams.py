class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagram = defaultdict(list)
        for eachString in strs:
            # create char array
            # count = [0]*26
            # for eachCharacter in eachString:
            #     count[ord(eachCharacter) -ord('a')]+=1
            # groupedAnagram[tuple(count)].append(eachString)

            sortedString = ''.join(sorted(eachString))
            groupedAnagram[sortedString].append(eachString)

        return groupedAnagram.values()


        