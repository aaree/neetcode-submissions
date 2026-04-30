class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        test= [-ans for ans in stones]
        heapq.heapify(test)
        while len(test)>1:
            one=-heapq.heappop(test)
            two=-heapq.heappop(test)
            new=one-two
            if new>0:
                heapq.heappush(test,-new)
        if len(test)>0:
            return -test[0]
        else:
            return 0
