class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[[] for i in range(len(nums)+1)]
        c=Counter(nums)
        final=[]
        for key, val in c.items():
            ans[val].append(key)
        for i in range(len(ans)-1,-1,-1):
            final.extend(ans[i])
            if len(final)>=k:
                break
        return final