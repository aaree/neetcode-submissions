class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        currSum=0
        maxSum=nums[0]
        for i in nums:
            currSum+=i
            if currSum>maxSum:
                maxSum=currSum
            if currSum<0:
                currSum=0
        return maxSum