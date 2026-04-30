class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=nums[0]
        cnt=0
        for i in nums:
            if i==n:
                cnt+=1
            else:cnt-=1
            if cnt<0:
                n=i
                cnt=0
        return n