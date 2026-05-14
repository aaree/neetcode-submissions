class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=nums[0]
        total=0
        for num in nums:
            total=max(0,total)
            total+=num
            maxSum=max(maxSum,total)
        
        return maxSum