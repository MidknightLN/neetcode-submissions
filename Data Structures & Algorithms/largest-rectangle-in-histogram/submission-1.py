class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        # 技巧：在末尾加一個 0，確保最後 stack 裡所有的柱子都會被彈出來結算
        heights.append(0)

        for idx, h in enumerate(heights):
            # 如果出現較小的 就要結算
            while stack and h < stack[-1][1]:
                # 高度
                curr_idx, curr_h = stack.pop()
                # 寬度
                width = idx if not stack else (idx - stack[-1][0] - 1)
                # 計算最大面積
                res = max(res, curr_h*width)
            stack.append((idx, h))
        return res
