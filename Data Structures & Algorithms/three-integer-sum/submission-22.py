class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(arr,target,start):
            left=start
            right=len(arr)-1
            ans=[]
            while right>left:
                total=arr[left]+arr[right]
                if total>target:
                    right-=1
                elif total<target:
                    left+=1
                elif total==target:
                    ans.append([-target,nums[left],nums[right]])
                    while right>left and (nums[left]==nums[left+1]):
                        left+=1
                    while right>left and (nums[right]==nums[right-1]):
                        right-=1
                    left+=1
                    right-=1
            return ans

        nums.sort()
        final=[]
        for i, val in enumerate(nums):
            if i==0 or nums[i]!=nums[i-1]:
                target=-val
                temp=twoSum(nums,target,i+1)
                final.extend(temp)
        return final