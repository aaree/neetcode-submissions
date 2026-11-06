class Solution:
    def twosum(self,target,start,arr):
        l=start
        r=len(arr)-1
        ans=[]
        while r>l:
            value=arr[l]+arr[r]
            if value>target:
                r-=1
            elif value<target:
                l+=1
            elif value==target:
                ans.append([-target,arr[l],arr[r]])
                while l<r and arr[l]==arr[l+1]:
                    l+=1
                while r>l and arr[r]==arr[r-1]:
                    r-=1
                r-=1
                l+=1
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        nums.sort()
        for i, num in enumerate(nums):
            if i==0 or nums[i]!=nums[i-1]:
                arr=self.twosum(-num,i+1,nums)
                ans+=arr

        return ans
