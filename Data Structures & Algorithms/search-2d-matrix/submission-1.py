class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2D binary search basically
        numRows = len(matrix)
        low = 0
        high = numRows - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                # go lower
                low = mid + 1
            else:
                # go higher
                high = mid - 1
        
        numCols = len(matrix[high])
        row = high
        low = 0
        high = numCols - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                # go lower
                low = mid + 1
            else:
                # go higher
                high = mid - 1
        
        return False
