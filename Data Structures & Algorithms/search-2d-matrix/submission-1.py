class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        trow = -1
        for sub in range(len(matrix)):
            if matrix[sub][-1] >= target:
                if matrix[sub][-1] == target:
                    return True
                trow = sub
                break
        # early return in case no target row found
        if trow == -1:
            return False
        
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = l + ((r-l) // 2)
            if matrix[trow][mid] == target:
                return True
            elif matrix[trow][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
                