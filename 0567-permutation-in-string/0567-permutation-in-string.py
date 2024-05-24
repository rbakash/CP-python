class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Length = len(s1)
        s2length = len(s2)

        if s1Length > s2length:
            return False

        # create frequency for s1
        s1Frequency = [0] * 26
        windowFrequency = [0] * 26
        for index in range(s1Length):
            s1Frequency[ord(s1[index]) - ord("a")] += 1
            windowFrequency[ord(s2[index]) - ord("a")] += 1

        # now check the frequency of characters of s1 in s2 of length s1
        for index in range(s2length - s1Length):
            # create frequency of new substring for the current Window
            # while end - start < s1Length:
            #     windowFrequency[ord(s2[end]) - ord("a")] += 1
            #     end += 1

            # compare the frequencies
            if self.matches(s1Frequency, windowFrequency):
                return True

            windowFrequency[ord(s2[index + s1Length]) - ord("a")] += 1
            windowFrequency[ord(s2[index]) - ord("a")] -= 1

        return self.matches(s1Frequency, windowFrequency)

    def matches(self, map1, map2) -> bool:
        for index in range(len(map2)):
            if map2[index] != map1[index]:
                # if map2.get(key, 0) !=0 :
                #     map2[key] =  map2[key]-1
                # start += 1
                # break
                return False

        return True
