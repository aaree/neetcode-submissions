class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i,val in enumerate(nums):
            opposite=target-val
            if opposite in s:
                return [s[opposite],i]
            s[val]=i