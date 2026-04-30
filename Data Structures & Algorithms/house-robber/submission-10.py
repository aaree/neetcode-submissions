class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        DP=[0]*(len(nums))
        DP[0]=nums[0]
        DP[1]=max(nums[0],nums[1])
        for i in range(2,len(DP)):
            DP[i]=max(nums[i]+DP[i-2],DP[i-1])
        return DP[-1]