class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(arr,target):
            ans=set()
            l=0
            r=len(arr)-1
            while l<r:
                total=arr[l]+arr[r]
                if total>target:
                    r-=1
                elif total<target:
                    l+=1
                elif total==target :
                    ans.add(tuple(sorted([-target,arr[l],arr[r]])))
                    l+=1
            return ans
        nums.sort()
        answer=set()
        for i in range(len(nums)):
            target=-nums[i]
            new_arr=nums[:i]+nums[i+1:]
            answ=twoSum(new_arr,target)
            answer.update(answ)
        final=[]
        for i in answer:
            final.append(list(i))
        return final