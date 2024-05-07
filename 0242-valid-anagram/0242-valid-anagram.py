class Solution:
    def isAnagram(self, string1: str, string2: str) -> bool:
        characterMap = defaultdict(int)

        for character in string1:
            characterMap[character] += 1

        for character in string2:
            characterMap[character] -= 1

        for key, value in characterMap.items():
            if characterMap[key] != 0:
                return False

        return True
