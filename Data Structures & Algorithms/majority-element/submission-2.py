class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target=len(nums)//2
        curr=nums[0]
        cnt=0
        for num in nums:
            if num==curr:
                cnt+=1
            else:
                cnt-=1
            if cnt<=0:
                curr=num
                cnt=1
        return curr