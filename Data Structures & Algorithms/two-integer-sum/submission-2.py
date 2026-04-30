class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            opposite=target-nums[i]
            if opposite in seen:
                return sorted([i,seen[opposite]])
            seen[nums[i]]=i
        