class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,val in enumerate(nums):
            opposite=target-val
            if opposite in seen:
                return [seen[opposite],i]
            seen[val]=i