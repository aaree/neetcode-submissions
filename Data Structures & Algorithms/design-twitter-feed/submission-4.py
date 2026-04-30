class Twitter:

    def __init__(self):
        self.following={}
        self.feeds={}
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.feeds:
            self.feeds[userId]=[]
        self.feeds[userId].append((-self.time,tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            self.following[userId]=set()
            self.following[userId].add(userId)
        temp=[]
        timeline=[]
        for id in self.following[userId]:
            if id not in self.feeds:
                self.feeds[id]=[]
            timeline.extend(self.feeds[id])
        heapq.heapify(timeline)
        while len(timeline)>0 and len(temp)<10:
            time,tweetId=heapq.heappop(timeline)
            temp.append(tweetId)
        return temp


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId]=set()
            self.following[followerId].add(followerId)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId]=set()
            self.following[userId].add(followerId)
        if followeeId in self.following[followerId] and followeeId!=followerId:
            self.following[followerId].remove(followeeId)