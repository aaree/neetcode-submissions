from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        ans=c.most_common(k)
        return [i[0] for i in ans]        