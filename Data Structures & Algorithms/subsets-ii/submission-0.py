class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def backtrack(arr,pointer):
            print(pointer)
            if pointer>=len(nums):
                ans.append(sorted(arr.copy()))
                return
            arr.append(nums[pointer])
            backtrack(arr,pointer+1)
            arr.pop()

            while pointer+1<len(nums) and nums[pointer]==nums[pointer+1]:
                pointer+=1
            backtrack(arr,pointer+1)
        backtrack([],0)
        return ans