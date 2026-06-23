class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS

        wordSet = set(wordList)
        # 如果目標單字根本不在字典裡，絕對無法到達
        if endWord not in wordSet:
            return 0

        # distance 字典：本質上就是我們圖結構中的「節點權重/距離」
        # 它同時兼顧了 visited 的功能（防止走回頭路）
        distance = {beginWord: 1}
        # Queue 裡面只存當前處理的單字（節點）
        queue = deque([beginWord])

        # 如果起點單字剛好在字典裡，記得先移除，避免走回頭路
        if beginWord in wordSet:
            wordSet.remove(beginWord)

        while queue:
            curr = queue.popleft()
            # 如果當前的 字就是目標就直接回傳距離
            if curr == endWord:
                return distance[curr]
            # 找可以轉換的鄰居
            for idx in range(len(curr)):
                original_char = curr[idx]

                for x in range(26):
                    char = chr(ord("a") + x)
                    if char == original_char:
                        continue

                    nxt = curr[:idx] + char + curr[idx + 1 :]

                    # 如果新單字存在於字典中，代表圖中存在一條邊 (curr -> nxt)
                    if nxt in wordSet:
                        # Condition: 如果這個相鄰節點「還沒被建立距離」
                        # 代表這是一條發現該節點的最短路徑
                        if nxt not in distance:
                            distance[nxt] = distance[curr] + 1
                            queue.append(nxt)
        
        return 0
        
