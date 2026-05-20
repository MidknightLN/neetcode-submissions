class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 做兩次二分法
        if not matrix:
            return False

        # 先針對垂直方向。
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = l + (r-l)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        row = r
        # 在針對水平方向
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r-l)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False