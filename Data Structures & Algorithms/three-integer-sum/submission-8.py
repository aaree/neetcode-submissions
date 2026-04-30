class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(arr,target,start):
            i=start
            j=len(arr)-1
            ans=set()
            while j>i:
                total=arr[i]+arr[j]
                if total>target:
                    j-=1
                elif total<target:
                    i+=1
                elif i!=j and total==target:
                    ans.add(tuple(sorted([arr[i],arr[j],-target])))
                    i+=1
            return ans

        nums.sort()
        allAns=set()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue            
            target=nums[i]
            arr=nums[:i]+nums[i+1:]
            temp=twoSum(nums,-nums[i],i+1)
            allAns.update(temp)
        final=[]
        for i in allAns:
            final.append(list(i))
        return final