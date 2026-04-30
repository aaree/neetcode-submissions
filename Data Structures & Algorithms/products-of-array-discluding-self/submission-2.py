class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward=[]
        reverse=[]
        fstart=1
        rstart=1
        for i in nums:
            forward.append(fstart)
            fstart*=i
        nums.reverse()
        for i in nums:
            reverse.append(rstart)
            rstart*=i
        reverse.reverse()
        final=[None]*len(nums)
        for i in range(len(nums)):
            final[i]=forward[i]*reverse[i]
        return final
