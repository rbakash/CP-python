class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(version) for version in version1.split(".")]
        version2 = [int(version) for version in version2.split(".")]
        # isV1Fewer = len(version1) < len(version2)

        for index in range(max(len(version1), len(version2))):
            v1Num = version1[index] if index < len(version1) else 0
            v2Num = version2[index] if index < len(version2) else 0

            if v1Num < v2Num:
                return -1
            elif v1Num > v2Num:
                return 1

        return 0

        # index = min(len(version1), len(version2))
        # total = sum(version2[index:] if isV1Fewer else version1[index:])
        # if total == 0 or (len(version2) == len(version1)):
        #     return 0
        # return -1 if isV1Fewer else 1

        v1Iterator, v2Iterator = 0, 0
        while v1Iterator < len(version1) or v2Iterator < len(version2):
            v1Num, v2Num = 0, 0
            while v1Iterator < len(version1) and version1[v1Iterator] != ".":
                v1Num = v1Num * 10 + int(version1[v1Iterator])
                v1Iterator += 1

            while v2Iterator < len(version2) and version2[v2Iterator] != ".":
                v2Num = v2Num * 10 + int(version2[v2Iterator])
                v2Iterator += 1
            print(v1Num, v2Num)
            if v1Num < v2Num:
                return -1
            elif v1Num > v2Num:
                return 1
            
            v1Iterator += 1
            v2Iterator += 1

        return 0
