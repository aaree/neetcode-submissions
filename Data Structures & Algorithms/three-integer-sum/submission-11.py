class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def TwoSum(target,start):
            l=start
            r=len(nums)-1
            ans=set()
            while r>l:
                total=nums[l]+nums[r]
                if total>target:
                    r-=1
                elif total<target:
                    l+=1
                else:
                    ans.add((-target,nums[l],nums[r]))
                    l+=1
                    r-=1
            return ans

        nums.sort()
        ans=[]
        for i, val in enumerate(nums):
            if val>0:
                break
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                a=TwoSum(-val,i+1)
                for tup in a:
                    ans.append(list(tup))
        return ans