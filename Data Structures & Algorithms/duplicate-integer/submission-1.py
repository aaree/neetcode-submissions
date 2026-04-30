class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        total=set()
        for i in nums:
            if i in total:
                return True
            total.add(i)
        return False