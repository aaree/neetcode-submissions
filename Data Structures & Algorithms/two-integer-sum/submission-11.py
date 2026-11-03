class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        opp={}
        for i, num in enumerate(nums):
            opposite=target-num
            if opposite in opp:
                return [opp[opposite],i]
            opp[num]=i
        return []