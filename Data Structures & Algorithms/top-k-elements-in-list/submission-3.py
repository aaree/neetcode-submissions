class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt={}
        final=[]
        ans=[]
        for i in nums:
            cnt[i]=cnt.get(i,0)+1
        for key, val in cnt.items():
            ans.append((val,key))
        heapq.heapify(ans)
        while len(ans)>k:
            heapq.heappop(ans)
        for cnt,val in ans:
            final.append(val)
        return final