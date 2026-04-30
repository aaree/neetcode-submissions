class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=r=0
        dic={}
        while r<len(nums):
            dic[nums[r]]=dic.get(nums[r],0)+1
            windowSize=r-l
            if windowSize>k:
                dic[nums[l]]-=1
                l+=1
            if dic[nums[r]]>1:
                return True
            r+=1
        return False
        