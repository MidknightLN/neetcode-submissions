class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2 ## 如果是偶數 代表 左邊一個 右邊一個 ## 如果是奇數 代表要取右邊最小的

        if m > n: # A小 B大
            A, B = nums2, nums1
            m, n = n, m
        else:
            A, B = nums1, nums2
        
        # 用短的來找
        l, r = 0, m
        while True:
            # A 貢獻的個數 + B 貢獻的個數 = half
            A_count = l + (r-l)//2
            B_count = half - A_count
            # short_mid + 1 + long_mid + 1 = half
            short_mid = A_count - 1
            long_mid = B_count - 1

            # 處理越界
            A_left = A[short_mid] if short_mid >= 0 else float('-inf')      
            A_right = A[short_mid + 1] if (short_mid + 1) < m else float('inf')
            
            B_left = B[long_mid] if long_mid >= 0 else float('-inf')
            B_right = B[long_mid + 1] if (long_mid + 1) < n else float('inf')

            # 交叉檢查
            if A_left <= B_right and B_left <= A_right:
                # 判斷奇數偶數
                if total % 2 == 1:
                    return min(A_right, B_right)
                else:
                    return((max(A_left, B_left) + min(A_right, B_right)) / 2.0)
            # 還沒滿足條件 就調整重切
            elif A_left > B_right:
                r = A_count - 1
            else:
                l = A_count + 1


