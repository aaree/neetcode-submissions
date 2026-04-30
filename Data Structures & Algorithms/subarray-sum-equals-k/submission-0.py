class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        values={0:1}
        total=0
        count=0
        for i,val in enumerate(nums):
            total+=val
            opposite=total-k
            if opposite in values:
                count+=values[opposite]
            values[total]=values.get(total,0)+1
        return count