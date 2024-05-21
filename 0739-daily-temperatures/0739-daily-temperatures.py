class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = []
        warmDays = [0]*len(temperatures)
        for index, temperature in enumerate(temperatures):

            while  monoStack and monoStack[-1][1] < temperature:
                (prevIndex, prevTemperature) = monoStack.pop()
                warmDays[prevIndex] = index - prevIndex
            monoStack.append((index, temperature))
        return warmDays
