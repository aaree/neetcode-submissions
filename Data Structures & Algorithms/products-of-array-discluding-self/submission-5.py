class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        prefixtotal=1
        suffix=[]
        suffixval=1
        final=[]
        for num in nums:
            prefix.append(prefixtotal)
            prefixtotal*=num
        for i in range(len(nums)-1,-1,-1):
            suffix.append(suffixval)
            suffixval*=nums[i]
        for i in range(len(nums)):
            final.append(prefix[i]*suffix[len(nums)-i-1])
        return final