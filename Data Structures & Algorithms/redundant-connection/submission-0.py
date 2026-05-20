class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 父親節點 紀錄表
        par = [i for i in range(len(edges)+1) ]
        # 樹的高度
        rank = [1] * (len(edges) + 1)

        # 先找出根結點
        def find(n):
            p=par[n]
            # 依序往上比對
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        # 比較edge 的兩邊 其根節點是否相同
        # union = 
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # 如果edge 兩邊都是相同 根節點 就代表造成迴圈了
            if p1 == p2:
                return True
            # 如果P1深度大於P2
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return False
        
        for n1, n2 in edges:
            if union(n1, n2):
                return [n1, n2]

            

            