class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        seen=set()
        target=sum(nums)/2
        for i in nums:
            updateSet=set()
            for j in seen:
                j+=i
                updateSet.add(j)
            if i not in seen:
                seen.add(i)
            seen.update(updateSet)
        return target in seen