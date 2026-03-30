class Twitter:

    def __init__(self):
        self.count = 0 # decrement so we can use max heap in python
        self.followMap = defaultdict(set) # userId to following set
        self.tweetMap = defaultdict(list) # userId to (count, tweetid) list

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    # use max heap (similar to merge k sorted lists)
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # get users following tweets first
        self.followMap[userId].add(userId)
        for user in self.followMap[userId]:
            if user in self.tweetMap:
                index = len(self.tweetMap[user]) - 1
                count, tweetId = self.tweetMap[user][index]
                minHeap.append([count, tweetId, user, index - 1])

        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, user, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[user][index]
                heapq.heappush(minHeap, [count, tweetId, user, index - 1])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
