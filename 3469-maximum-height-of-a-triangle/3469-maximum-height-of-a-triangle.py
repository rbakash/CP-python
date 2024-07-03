class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        maxLength = 0
        for index in range(2):
            isRed = True if index == 0 else False
            level = 1
            tempRed = red
            tempBlue = blue
            while tempRed >= level or tempBlue >= level:

                if not isRed:
                    if tempBlue <= 0 or tempBlue < level:
                        break
                    tempBlue -= level
                else:
                    if tempRed <= 0 or tempRed < level:
                        break
                    tempRed -= level
                level += 1
                isRed = not isRed
                print(isRed, level, tempRed, blue)
            print("for ", index)
            maxLength = max(maxLength, level - 1)
        return maxLength
