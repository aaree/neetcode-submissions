class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        seen=set()
        def backtrack(pointer,arr):
            if tuple(sorted(arr)) not in seen:
                ans.append(sorted(arr.copy()))
                seen.add(tuple(sorted(arr)))
            if pointer>=len(nums):
                return
            backtrack(pointer+1,arr)
            arr.append(nums[pointer])
            backtrack(pointer+1,arr)
            arr.pop()
        backtrack(0,[])
        return ans        