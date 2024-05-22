class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        
        if rows == 0:
            return False

        columns = len(matrix[0])
        low = 0
        high = rows * columns - 1

        while low <= high:
            mid = high - low // 2
            pivotElement = matrix[mid // columns][mid % columns]
            if target == pivotElement:
                return True
            if target < pivotElement:
                high = mid - 1
            else:
                low = mid + 1
        return False
