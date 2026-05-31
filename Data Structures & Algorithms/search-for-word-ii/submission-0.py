class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr.child.setdefault(c, TrieNode()) # 檢查是否存在，如果不存在就建立
            curr = curr.child[c] # 移動到該NODE 下
        curr.is_end = word # 直接把整個單字存到 結尾

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # init
        if not board:
            return []
        
        # 將所有 待找單字 做成 TrieNode
        tree = WordDictionary()
        for word in words:
            tree.addWord(word)
        
        # 主要的DFS
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c, node):
            # 用當前啟始字元 找 當前的node
            curr_char = board[r][c]
            curr_node = node.child[curr_char]

            # 檢查是否拼出完整的單字
            if curr_node.is_end:
                res.append(curr_node.is_end)
                curr_node.is_end = False # 清空

            # 標記當前位置已訪問，防走回頭路
            board[r][c] = "#"
            # 往上下左右探索
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                
                # 邊界檢查與關鍵剪枝：下一格字母必須存在於當前 Trie 節點的 child 中
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    if board[nr][nc] in curr_node.child:
                        dfs(nr, nc, curr_node)
            # 後退（回溯）：拔掉圖釘、恢復現場，讓後續其他平行路徑可以使用這個字母
            board[r][c] = curr_char

            # 【進階高效剪枝】如果這個子節點已經沒有任何後續單字了，直接拔掉它
            if not curr_node.child:
                node.child.pop(curr_char)
        
        # 遍歷 Grid 上的所有位置 從該位子作為起點開始找
        rows, cols = len(board), len(board[0])
        res = []
        for r in range(rows):
            for c in range(cols):
                # 初始字元匹配上再開始
                if board[r][c] in tree.root.child:
                    # 啟動 DFS，把座標以及 Trie 的根節點傳進去
                    dfs(r, c, tree.root)
        return res
        
        