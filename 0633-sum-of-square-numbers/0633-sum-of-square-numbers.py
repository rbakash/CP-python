class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # get all the numbers less than c**0.5
        numbers =[]
        for num in range(int(c**0.5)+1):
            numbers.append(num)
        print(numbers)

        # See if you can make c from numbers
        start,end = 0,len(numbers)-1
        while start <= end:
            square = numbers[start]**2 + numbers[end]**2
            if square == c:
                return True
            elif square < c:
                start+=1
            else:
                end-=1

        return False