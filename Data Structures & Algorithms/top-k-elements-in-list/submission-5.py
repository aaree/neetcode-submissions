class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket=[[]for i in range(len(nums)+1)]
        c=Counter(nums)
        for key, val in c.items():
            bucket[val].append(key)
        final=[]
        for i in range(len(bucket)-1,-1,-1):
            if len(bucket[i])>0:
                final.extend(bucket[i])
        return final[:k]