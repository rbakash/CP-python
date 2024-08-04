class Solution:
    def intToRoman(self, num: int) -> str:
        pattern={
            1000:"M",
            900:"CM",
            500:"D",
            400:"CD",
            100:"C",
            90:"XC",
            50:"L",
            40:"XL",
            10:"X",
            9:"IX",
            5:"V",
            4:"IV",
            1:"I"   
        }
        romanDigits=[]
        for romanNum,symbol in pattern.items():
            if num == 0:
                break
            count, num = divmod(num,romanNum)
            romanDigits.append(symbol*count)
        return "".join(romanDigits)
