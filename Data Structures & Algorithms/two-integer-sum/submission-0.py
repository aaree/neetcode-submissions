class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}
        for i in range(len(nums)):
            opposite=target-nums[i]
            if opposite in ans:
                return [ans[opposite],i]
            ans[nums[i]]=i
        return []