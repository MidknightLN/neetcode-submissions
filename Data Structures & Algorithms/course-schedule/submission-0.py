class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 用DFS 查找 確認所有課程需求沒有產生回圈

        # 先把所有課程整理成 Map (Trie Tree)
        courseMap = defaultdict(list)
        for course, pre in prerequisites:
            courseMap[course].append(pre)

        # 用set 紀錄當前看過哪些
        seen = set()
        def dfs(course):
            # 看見已經看過的就代表回圈了
            if  course in seen:
                return False
            if courseMap[course] == []:
                return True
            
            seen.add(course)
            for pre in courseMap[course]:
                if not dfs(pre):
                    return False
            seen.remove(course)
            # 剪枝 如果已經確認 他的pre都是安全的就直接刪除。
            courseMap[course] = []
            return True


        # Main loop
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True



        
