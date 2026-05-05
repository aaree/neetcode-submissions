class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(target, nums, start):
            l=start
            r=len(nums)-1
            ans=[]
            while r>l:
                total=nums[l]+nums[r]
                if total>target:
                    r-=1
                elif total<target:
                    l+=1
                elif total==target:
                    ans.append([-target,nums[l],nums[r]])
                    while r>l and nums[l]==nums[l+1]:
                        l+=1
                    while r>l and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
                    l+=1

            return ans

        nums.sort()
        ans=[]
        for i, num in enumerate(nums):
            if num>0:
                break
            if i==0 or nums[i]!=nums[i-1]:
                target=-num
                temp=twoSum(target, nums, i+1)
                ans.extend(temp)
        return ans