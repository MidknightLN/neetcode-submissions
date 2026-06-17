class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological Sort (Kahn's Algorithm)
        # 入度 (Indegree) —— 「我的先修限制」
        # 出度 (Outdegree) —— 「我是誰的絆腳石 / 解鎖關鍵」


        indegree = [0 for _ in range(numCourses)]
        outdegree = defaultdict(list)

        # 把prerequisites 轉換成 出入度地圖
        for course, preq in prerequisites:
            indegree[course] += 1
            outdegree[preq].append(course)
        
        # 找到所有 indegree=0的 課程
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            for c in outdegree[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
        
        return all(i == 0 for i in indegree)
        

        