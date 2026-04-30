class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(target,start):
            l=start
            r=len(nums)-1
            while r>l:
                total=nums[l]+nums[r]
                if l>start and nums[l]==nums[l-1]:
                    l+=1
                    continue
                elif total>target:
                    r-=1
                elif total<target:
                    l+=1
                elif total==target:
                    ans.append(sorted([nums[l],nums[r],-target]))
                    l+=1

        nums.sort()
        ans=[]
        for i,val in enumerate(nums):
            if val>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            twoSum(-val,i+1)
        

        return ans