class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        grouping=[[] for i in range(len(nums)+1)]
        c=Counter(nums)
        for key, val in c.items():
            grouping[val].append(key)
        answer=[]
        for i in range(len(grouping)-1,-1,-1):
            if len(answer)<k:
                answer.extend(grouping[i])
        return answer