class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums={}
        for i, val in enumerate(nums):
            opp=target-val
            if opp in sums:
                return [sums[opp],i]
            sums[val]=i
