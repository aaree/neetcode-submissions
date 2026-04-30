class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(target,start):
            l=start
            ans=set()
            r=len(nums)-1
            while r>l:
                total=nums[l]+nums[r]
                if total>target:
                    r-=1
                if total<target:
                    l+=1
                if total==target:
                    ans.add(tuple([-target,nums[l],nums[r]]))
                    r-=1
                    l+=1
            return ans


        nums.sort()
        final=[]
        for i,num in enumerate(nums):
            if num>0:
                break
            if i==0 or (nums[i]!=nums[i-1]):
                s=twoSum(-num,i+1)
                for i in s:
                    final.append(list(i))
        return final