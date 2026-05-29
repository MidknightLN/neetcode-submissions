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
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.is_end = True

    def search(self, word: str) -> bool:

        def dfs(index, curr):
            if index == len(word):
                return curr.is_end

            c = word[index]

            if c == '.':
                for child in curr.child.values():
                    if dfs(index+1, child):
                        return True
                return False
            elif c not in curr.child:
                return False
            else:
                return dfs(index + 1, curr.child[c])
        return dfs(0, self.root)
        
