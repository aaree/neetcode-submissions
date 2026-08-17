class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr={}
        for i, val in enumerate(nums):
            opposite=target-val
            if opposite in arr:
                return [arr[opposite],i]
            arr[val]=i
        