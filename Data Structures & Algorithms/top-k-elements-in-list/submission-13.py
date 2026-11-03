class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        ans=[[] for _ in range(len(nums)+1)]
        for key, val in c.items():
            ans[val].append(key)
        final=[]
        for i in range(len(ans)-1,-1,-1):
            if len(ans[i])>0 and k>=len(ans[i]):
                final+=ans[i]
                k-=len(ans[i])
            elif len(ans[i])>0 and k<len(ans[i]):
                for i in range(k):
                    val=ans[i].pop()
                    final.append(val)
        return final