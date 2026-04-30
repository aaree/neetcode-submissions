class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        temp=[]
        heapq.heapify(temp)
        for key, val in c.items():
            heapq.heappush(temp,(val,key))
        while len(temp)>k:
            heapq.heappop(temp)
        final=[]
        for val,key in temp:
            final.append(key)
        return final