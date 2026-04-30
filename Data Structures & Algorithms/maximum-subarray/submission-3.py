class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        mintotal=math.inf
        maxtotal=-math.inf
        total=0
        for num in nums:
            mintotal=min(mintotal,total)
            total+=num            
            maxtotal=max(maxtotal,total-mintotal)
        return maxtotal