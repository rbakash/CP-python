class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(version) for version in version1.split(".")]
        version2 = [int(version) for version in version2.split(".")]
        isV1Fewer = len(version1) < len(version2)
        print(version1, version2)
        for index in range(min(len(version1), len(version2))):
            if version1[index] != version2[index]:
                return 1 if version1[index] > version2[index] else -1
        print(index)
        index = min(len(version1), len(version2))
        total = sum(version2[index:] if isV1Fewer else version1[index:])
        if total == 0 or (len(version2) == len(version1)):
            return 0
        return -1 if isV1Fewer else 1
