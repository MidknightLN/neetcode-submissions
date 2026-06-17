class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological Sort (Kahn's Algorithm)
        # 入度 (Indegree) —— 「我的先修限制」
        # 出度 (Outdegree) —— 「我是誰的絆腳石 / 解鎖關鍵」
        indegreed = [0 for _ in range(numCourses)]
        outdegreed = defaultdict(list)

        for course, preq in prerequisites:
            indegreed[course] += 1
            outdegreed[preq].append(course)
        
        # 把所有 Indegree = 0 的放入deque 開始查找
        q = deque()
        for idx, deg in enumerate(indegreed):
            if deg == 0:
                q.append(idx)
        
        res = []
        while q:
            course = q.popleft()
            res.append(course)

            for c in outdegreed[course]:
                indegreed[c] -= 1
                if indegreed[c] == 0:
                    q.append(c)
        
        return res if len(res) == numCourses else []