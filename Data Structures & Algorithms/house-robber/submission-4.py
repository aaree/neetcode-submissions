class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        DP=[None]*len(nums)
        DP[0]=nums[0]
        DP[1]=max(nums[1],nums[0])
        for i in range(2,len(DP)):
            val=max(DP[i-1],DP[i-2]+nums[i])
            DP[i]=val
        return DP[-1]