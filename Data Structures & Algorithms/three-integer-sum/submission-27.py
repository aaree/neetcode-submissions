class Solution:
    def twoSum(self,start,target,nums):
        l=start
        r=len(nums)-1
        final=[]
        while r>l:
            total=nums[l]+nums[r]
            if total>target:
                r-=1
            elif total<target:
                l+=1
            elif total==target:
                final.append([-target,nums[l],nums[r]])
                while r>l and nums[l]==nums[l+1]:
                    l+=1
                while r>l and nums[r]==nums[r-1]:
                    r-=1
                l+=1
                r-=1
        return final
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i, val in enumerate(nums):
            if val>0:
                break
            if i==0 or (nums[i]!=nums[i-1]):
                target=-val
                temp=self.twoSum(i+1,target,nums)
                ans.extend(temp)
        return ans