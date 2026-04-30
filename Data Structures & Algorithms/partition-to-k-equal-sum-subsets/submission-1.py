class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        ans=[0]*k
        if sum(nums)%k!=0:
            return False
        target=sum(nums)/k
        nums.sort(key=lambda x:-x)
        def dfs(arr,pointer):
            if pointer==len(nums):
                if sum(arr)==k*target:
                    return True
                else:
                    return False
            val=nums[pointer]
            for i in range(len(arr)):
                alreadyTried=False
                for j in range(i):
                    if arr[j]==arr[i]:
                        alreadyTried=True
                if alreadyTried:
                    continue
                if arr[i]+val<=target:
                    arr[i]+=val
                    if dfs(arr,pointer+1):
                        return True
                    arr[i]-=val
            return False
        return dfs(ans,0)
