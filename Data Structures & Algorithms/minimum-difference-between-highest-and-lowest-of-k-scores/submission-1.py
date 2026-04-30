class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff=0
        minDiff=9999999
        l=0
        r=1
        while r<len(nums):
            d=abs(nums[r]-nums[r-1])
            diff+=d
            while r-l+1>k:
                l+=1
                d=abs(nums[l]-nums[l-1])
                diff-=d
            if r-l+1==k:
                minDiff=min(diff,minDiff)
            r+=1
        return 0 if minDiff==9999999 else minDiff