class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        test={}
        for num,val in enumerate(nums):
            opposite=target-val
            if opposite in test:
                return [test[opposite],num]
            else:
                test[val]=num