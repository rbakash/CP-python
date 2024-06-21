class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse=True)
        currentBoxCapacity=0
        boxes =0
        for eachCapacity in capacity:
            
            if currentBoxCapacity >= apples:
                break
            currentBoxCapacity += eachCapacity
            boxes+=1
        return boxes