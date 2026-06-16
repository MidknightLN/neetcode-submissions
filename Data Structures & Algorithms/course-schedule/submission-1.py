class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        # 先建立map
        for c, preq in prerequisites:
            courseMap[c].append(preq)
        
        # 這邊用 seen 紀錄看過什麼  dfs 回傳是否 可以正常查找完畢 沒有產生回圈
        seen = set()
        def dfs(c):
            # 邊界條件
            if c in seen:
                return False
            # 正常結束條件
            if courseMap[c] == []:
                return True
            
            # 主要回圈部分
            seen.add(c)
            for q in courseMap[c]:
                if not dfs(q):
                    return False
            seen.remove(c)
            courseMap[c] = []
            return True

        for i in range(numCourses):
            # 如果每個課程的要求產生回圈就終止
            if not dfs(i):
                return False
        return True
