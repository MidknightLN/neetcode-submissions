class TimeMap:
    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if not self.time_dict.get(key):
            return res
        else:
            q = self.time_dict[key]
            l, r = 0, len(q) - 1
            while l <= r:
                mid = l + (r - l)//2
                if q[mid][0] == timestamp:
                    return q[mid][1]
                if q[mid][0] < timestamp:
                    res = q[mid][1]  ## 合法數值 更新後 繼續找
                    l = mid + 1
                else:

                    r = mid - 1
        
            return res