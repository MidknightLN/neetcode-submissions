class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        rows, cols = len(matrix), len(matrix[0])
        l, r =  0, rows*cols-1

        while l <= r:
            mid = l + (r-l)//2
            tr, tc = mid // cols, mid % cols
            if matrix[tr][tc] == target:
                return True
            elif matrix[tr][tc] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        return False