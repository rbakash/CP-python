class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the inflection point
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[-1]:
                low = mid + 1
            else:
                high = mid - 1

        inflectionPoint = low
        degreeOfRotation = n - inflectionPoint

        print(inflectionPoint)
        print(degreeOfRotation)

        low, high = (inflectionPoint + degreeOfRotation) % n, (inflectionPoint + degreeOfRotation - 1)%n

        while low <= high:
            mid = low + (high - low) // 2
            adjustedMid = (mid - degreeOfRotation) % n
            if nums[adjustedMid] == target:
                return adjustedMid
            elif nums[adjustedMid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1
        # compare the tagret
