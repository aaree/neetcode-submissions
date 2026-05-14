class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        seen=set()
        def backtrack(pointer,arr):
            if tuple(arr) not in seen:
                ans.append(arr.copy())
                seen.add(tuple(arr))
            if pointer>=len(nums):
                return
            backtrack(pointer+1,arr)
            arr.append(nums[pointer])
            backtrack(pointer+1,arr)
            arr.pop()
        backtrack(0,[])
        return ans