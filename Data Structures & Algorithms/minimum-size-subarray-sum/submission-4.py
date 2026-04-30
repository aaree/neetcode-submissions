class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowSum=0
        windowSize=0
        r=l=0
        min_window=999999
        while r<len(nums):
            windowSum+=nums[r]
            while windowSum>=target:
                if windowSum>=target:
                    windowSize=r-l+1
                    min_window=min(min_window,windowSize)
                windowSum-=nums[l]
                l+=1
            r+=1
        return 0 if min_window==999999 else min_window