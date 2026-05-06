class Twitter:

    def __init__(self):
        self.cache={}
        self.follow1={}
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.cache:
            self.cache[userId]=[]
        self.cache[userId].append((-self.time,tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        stack=[]
        ans=[]
        cnt=10
        if userId not in self.follow1:
            self.follow1[userId]=set()
        for follow in self.follow1[userId]:
            if follow not in self.cache:
                self.cache[follow]=[]
            temp=self.cache[follow]
            stack.extend(temp)
        if userId in self.cache:
            stack.extend(self.cache[userId])
        heapq.heapify(stack)
        while cnt>0 and len(stack)>0:
            t=heapq.heappop(stack)
            ans.append(t[1])
            cnt-=1
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow1:
            self.follow1[followerId]=set()
        if followerId!=followeeId:
            self.follow1[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow1:
            self.follow1[followerId]=set()
        if followeeId in self.follow1[followerId]:
            self.follow1[followerId].remove(followeeId)
