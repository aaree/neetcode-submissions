class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        seen=set()
        def backtrack(arr,seen):
            if len(arr)==len(nums):
                ans.append(arr.copy())
            for i in nums:
                if i not in seen:
                    arr.append(i)
                    seen.add(i)
                    backtrack(arr,seen.copy())
                    arr.pop()
                    seen.remove(i)
        backtrack([],seen)
        return ans