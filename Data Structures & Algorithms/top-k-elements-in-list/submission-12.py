class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        temp=[]
        for key, val in c.items():
            heapq.heappush(temp,(-val,key))
        final=[]
        while len(final)<k:
            num,val=heapq.heappop(temp)
            final.append(val)
        return final