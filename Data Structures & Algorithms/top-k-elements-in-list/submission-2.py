from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans={}
        for i in nums:
            ans[i]=ans.get(i,0)+1
        ans2=[]
        for key,val in ans.items():
            ans2.append((val,key))
        heapq.heapify(ans2)
        while len(ans2)>k:
            heapq.heappop(ans2)
        final=[]
        for i in ans2:
            final.append(i[1])
        return final