class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        new=heapq.nlargest(k,nums)
        return new[-1]