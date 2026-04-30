import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        opp=[-i for i in gifts]
        heapq.heapify(opp)
        for i in range(k):
            temp=-heapq.heappop(opp)
            temp=math.floor(math.sqrt(abs(temp)))
            heapq.heappush(opp,-temp)
        cnt=0
        for i in opp:
            cnt+=i
        return abs(cnt)