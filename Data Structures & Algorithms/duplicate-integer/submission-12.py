class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nondupe=set()
        for num in nums:
            if num in nondupe:
                return True
            nondupe.add(num)
        return False