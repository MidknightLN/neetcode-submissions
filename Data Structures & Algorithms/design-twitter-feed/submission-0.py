class Twitter:

    def __init__(self):
        self.time = 0 # 時間戳 #因為 tweetId 不代表時間順序
        self.tweetMap = defaultdict(list) # 紀錄每個人的post [time, tweetId]
        self.followMap = defaultdict(set) # 紀錄每個人的followee ()


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [-(time), tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [-(time), tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # 只要確保不是自己追蹤自己，就可以直接 add，重複了 set 會自動忽略
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # 必須先確認存在才能移除。
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
