class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        temp=[[]for i in range(len(nums)+1)]
        ans=[]
        for key, val in c.items():
            temp[val].append(key)
        print(temp)
        for i in range(len(temp)-1,-1,-1):
            if len(temp[i])>0:
                ans.extend(temp[i])
            if len(ans)==k:
                return ans