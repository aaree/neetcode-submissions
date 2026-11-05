class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward=[]
        reverse=[]
        fval=1
        rval=1
        for i in range(0,len(nums)):
            forward.append(fval)
            fval*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            reverse.append(rval)
            rval*=nums[i]
        final=[]
        for i in range(len(forward)):
            final.append(forward[i]*reverse[len(reverse)-i-1])
        return final