class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # 紀錄 每個 node 的記憶體位置
        # 先建立兩個虛擬節點 方便查找頭跟尾
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # 把這兩個節點相互鏈結
        self.head.next = self.tail
        self.tail.prev = self.head # 尾巴到頭 是逆序 用 prev
    
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        # 插入一個新的節點到 最常用的位置 也就是head>>
        # 以下這四行要同時處理 否則需要暫存
        nxt = self.head.next # 先記錄原本第一個node
        self.head.next = node
        node.next = nxt
        nxt.prev = node
        node.prev = self.head


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self.remove(lru_node)
            del self.cache[lru_node.key]

        
