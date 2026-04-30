class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(arr,pointer):

            while pointer<len(nums):
                arr.append(nums[pointer])
                backtrack(arr.copy(),pointer+1)
                arr.pop()
                pointer+=1
            if pointer==len(nums):
                ans.append(arr)                
        backtrack([],0)
        return ans