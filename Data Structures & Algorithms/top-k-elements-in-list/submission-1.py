from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt={}
        for i in nums:
            cnt[i]=cnt.get(i,0)+1
        ans=[]
        for key,value in cnt.items():
            ans.append((value,key))
        heapq.heapify(ans)
        while len(ans)>k:
            heapq.heappop(ans)
        final=[]
        for i in ans:
            final.append(i[1])
        return final