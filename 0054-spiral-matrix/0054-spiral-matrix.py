class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,columns = len(matrix),len(matrix[0])
        # Initialize the matrix with zeros
        # matrix = [[0] * columns for _ in range(rows)]
        result = []
        
        # Define the boundaries
        top, bottom, left, right = 0, rows - 1, 0, columns - 1
        num = 1  # Start filling with number 1
        
        while top <= bottom and left <= right:
            # Fill the top row
            for i in range(left, right + 1):
                # matrix[top][i] = num
                result.append(matrix[top][i])
                num += 1
            top += 1
            
            # Fill the right column
            for i in range(top, bottom + 1):
                # matrix[i][right] = num
                result.append(matrix[i][right])
                num += 1
            right -= 1
            
            if top <= bottom:
                # Fill the bottom row
                for i in range(right, left - 1, -1):
                    # matrix[bottom][i] = num
                    result.append(matrix[bottom][i])
                    num += 1
                bottom -= 1
            
            if left <= right:
                # Fill the left column
                for i in range(bottom, top - 1, -1):
                    # matrix[i][left] = num
                    result.append(matrix[i][left])
                    num += 1
                left += 1
        
        return result