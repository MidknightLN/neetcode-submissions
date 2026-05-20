class LRUCache:
    # 使用雙向鏈結表 可以自己實作 或者使用 OrderDict << 現成套件 
    from collections import OrderedDict

    def __init__(self, capacity: int):
        # 初始化容量
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # 取得
        if key not in self.cache:
            return -1
        
        # 關鍵：將最近使用的 key 移到最右端（代表最新使用）
        # 內部底層是用 O(1) 的指標操作直接把中間的節點抽出來放到最後面
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # 放入 另外，如果 超出容量 要將最少使用的刪除
        if key in self.cache:
            # 如果 key 已存在，先移到最右端
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
                # last=False 代表彈出最左端（最舊）的資料
                # 內部底層也是 O(1) 操作
                self.cache.popitem(last=False)
        