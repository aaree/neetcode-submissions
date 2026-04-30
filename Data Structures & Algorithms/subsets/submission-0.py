class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        seen=[]
        def backtrack(num):
            nonlocal seen
            if num in seen:
                return False
            seen.append(num.copy())
            for i in range(len(num)):
                val=num.pop(i)
                backtrack(num.copy())
                num.insert(i,val)
        backtrack(nums)
        
        return list(seen)
