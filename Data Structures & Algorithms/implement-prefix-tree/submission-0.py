class TrieNode:
    def __init__(self):
        # Stores references to child nodes (character -> TrieNode)
        self.child = {}
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            # 如果沒有這個新的字 就增加
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        # 記得把最後一個字元 設定成結束
        curr.is_end = True

    def search(self, word: str) -> bool:
        # 這邊必須要全部匹配上。
        curr = self.root
        for c in word:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        # 這裡不用全部匹配
        # 這邊必須要全部匹配上。
        curr = self.root
        for c in prefix:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return True
        