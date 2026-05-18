class Solution:
    def twoSum(self, start, target, nums):
        left=start
        right=len(nums)-1
        arr=[]
        while right>left:
            total=nums[right]+nums[left]
            if total>target:
                right-=1
            elif total<target:
                left+=1
            elif total==target:
                arr.append([-target,nums[left],nums[right]])
                while right>left and nums[left]==nums[left+1]:
                    left+=1
                while right>left and nums[right]==nums[right-1]:
                    right-=1
                left+=1
                right-=1
        return arr

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final=[]
        for i, val in enumerate(nums):
            if val>0:
                break
            if i==0 or nums[i]!=nums[i-1]:
                target=-val
                temp=self.twoSum(i+1,target,nums)
                final.extend(temp)
        return final