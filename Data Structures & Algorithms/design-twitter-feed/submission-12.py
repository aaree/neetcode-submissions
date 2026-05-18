class Twitter:

    def __init__(self):
        self.database={}
        self.following={}
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.database:
            self.database[userId]=[]
        self.time+=1
        self.database[userId].append((-self.time,tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            self.following[userId]=set()
            self.following[userId].add(userId)
        temp=[]
        feed=[]
        for tid in self.following[userId]:
            if tid in self.database:
                userFeed=self.database[tid]
            else:
                userFeed=[]
            for tweet in userFeed:
                heapq.heappush(temp,tweet)
        
        while temp and len(feed)<10:
            time, val=heapq.heappop(temp)
            feed.append(val)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId]=set()
            self.following[followerId].add(followerId)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId]=set()
            self.following[followerId].add(followerID)
        if followerId!=followeeId:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)

        
