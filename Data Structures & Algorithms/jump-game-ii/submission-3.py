class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        i=0
        cnt=1
        while i<len(nums)-1:
            maxjump=0
            maxjumploc=0
            print(maxjump)
            curr=i
            while i<min(len(nums)-1,curr+nums[curr]):
                i+=1
                if (i+nums[i])>=(maxjumploc+maxjump):
                    maxjump=nums[i]
                    maxjumploc=i
                if i==len(nums)-1:
                    return cnt
            i=maxjumploc
            cnt+=1                
        return cnt