class Twitter:

    def __init__(self):
        self.time = 0
        self.user_tweets = defaultdict(list)
        self.user_followees = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_followees:
            self.user_followees[userId].add(userId)
        self.user_tweets[userId].append((self.time, tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for followees in self.user_followees[userId]:
            for tweet in self.user_tweets[followees]:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)
        heap.sort(key=lambda x: -x[0])
        result = [x[1] for x in heap]
        print(result)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_followees:
            self.user_followees[followerId].add(followerId)
        self.user_followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_followees:
            self.user_followees[followerId].add(followerId)
        if followerId == followeeId:
            return
        if followeeId in self.user_followees[followerId]:
            self.user_followees[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)